
import base64
from datetime import datetime
from typing import Union

# import psycopg2


def get_paginated_things(
    # db_conn,
    page_cursor: str = "MTcyMDY5MjMyMy4zMDQ4Nzg6NzI0MDIwNzc=",
    page_size: int = 20,
    next_page: bool = False,
    device_status: int = 0,
    device_type: int = -1,
) -> tuple:
    # cursor = db_conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    if page_cursor:
        page_cursor_ts_str, page_cursor_no_str = (
            base64.b64decode(page_cursor).decode("utf-8").split(":")
        )
        print(page_cursor_no_str)
        page_cursor_ts = datetime.utcfromtimestamp(float(page_cursor_ts_str))
        page_cursor_no = int(page_cursor_no_str)
    else:
        page_cursor_ts, page_cursor_no = datetime.utcnow(), 123399999

    base_query = """
        Select Thing.created, Thing.activation_ts, Thing.id, Thing.serial_no, 
        Thing.f_ver, Thing.model_id, (ThingState.conn_state ->> 'connected')::boolean AS connected,
        ThingState.conn_ts, Thingstate.state_ts, ACModel.product_id, ACModel.remote_type, 
        AppUser.name AS customer_name
        FROM Thing
        LEFT JOIN ThingState ON Thing.id = ThingState.thing_id
        LEFT JOIN ACModel ON Thing.model_id = ACModel.id
        LEFT JOIN UserThingMapping ON Thing.id = UserThingMapping.thing_id
        LEFT JOIN AppUser ON UserThingMapping.user_id = AppUser.id
        WHERE (UserThingMapping.user_type IS NULL OR UserThingMapping.user_type = 0) 
    """

    if device_type >= 0 :
        base_query = (
            base_query
            + """
        AND Thing.type = {device_type}
        """.format(
            device_type=device_type
            )
        )

    if device_status == 1:
        base_query = (
            base_query
            + """
        AND Thing.activation_ts IS NOT NULL
        AND (ThingState.conn_state ->> 'connected')::boolean is true
        """
        )
    elif device_status == 2:
        base_query = (
            base_query
            + """
        AND Thing.activation_ts IS NOT NULL
        AND (ThingState.conn_state ->> 'connected')::boolean is false
        """
        )
    elif device_status == 3:
        base_query = (
            base_query
            + """
        AND Thing.activation_ts IS NOT NULL
        """
        )

    if device_status == 3:
        if next_page:
            paginated_device_query = (
                base_query
                + """
                AND Thing.activation_ts < '{page_cursor_ts}'
                ORDER BY Thing.activation_ts DESC LIMIT {page_size};
            """.format(
                    page_cursor_ts=page_cursor_ts, page_size=page_size
                )
            )
        else:
            paginated_device_query = (
                base_query
                + """
                AND Thing.activation_ts > '{page_cursor_ts}'
                ORDER BY Thing.activation_ts LIMIT {page_size};
            """.format(
                    page_cursor_ts=page_cursor_ts, page_size=page_size
                )
            )

        # cursor.execute(paginated_device_query, {"device_type": int(device_type)})
        # results = cursor.fetchall()
        # cursor.close()
        # if not results:
        #     return ([], None)

        # page_cursor = base64.b64encode(
        #     (
        #         str(results[-1:][0]["activation_ts"].timestamp())
        #         + ":"
        #         + str(results[-1:][0]["serial_no"])
        #     ).encode("utf-8")
        # ).decode("utf-8")

    else:
        if next_page:
            paginated_device_query = (
                base_query
                + """
                AND Thing.created <= '{page_cursor_ts}'
                AND Thing.serial_no < '{page_cursor_no}'
                ORDER BY Thing.created DESC, Thing.serial_no DESC LIMIT {page_size};
            """.format(
                    page_cursor_ts=page_cursor_ts,
                    page_size=page_size,
                    page_cursor_no=page_cursor_no,
                )
            )
        else:
            paginated_device_query = (
                base_query
                + """
                AND Thing.created >= '{page_cursor_ts}'
                AND Thing.serial_no > '{page_cursor_no}'
                ORDER BY Thing.created, Thing.serial_no LIMIT {page_size};
            """.format(
                    page_cursor_ts=page_cursor_ts,
                    page_size=page_size,
                    page_cursor_no=page_cursor_no,
                )
            )

        # cursor.execute(paginated_device_query, {"device_type": int(device_type)})
        # results = cursor.fetchall()
        # cursor.close()
        # if not results:
        #     return ([], None)

        # page_cursor = base64.b64encode(
        #     (
        #         str(results[-1:][0]["created"].timestamp())
        #         + ":"
        #         + str(results[-1:][0]["serial_no"])
        #     ).encode("utf-8")
        # ).decode("utf-8")

    # page_cursor = None if len(results) != page_size else page_cursor
    return paginated_device_query, page_cursor

print(get_paginated_things()[0])