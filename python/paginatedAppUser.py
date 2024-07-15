import base64
from datetime import datetime

def get_paginated_app_user(
    page_cursor: str = "MTcyMDY5MjMyMy4zMDQ4Nzg6NzI0MDIwNzc=", 
    page_size: int = 15, 
    next_page: bool = True, 
    filter_type: int = 0,
) -> tuple:
    # cursor = db_conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    if page_cursor:
        cursor_string = base64.b64decode(page_cursor).decode("utf-8")
        ts_string, last_id = cursor_string.split(":")
        created = datetime.utcfromtimestamp(float(ts_string))
    else:
        created, last_id = datetime.utcnow(), "ffffffff-ffff-ffff-ffffffffffff"

    paginated_user_query = """
        WITH PaginatedAppUser AS (
            SELECT id, name, countrycode, created, deleted, config, tuya_user_id
            FROM AppUser
    """

    if filter_type >= 0:
        paginated_user_query = (
            paginated_user_query
            + """
            JOIN UserThingMapping ON AppUser.id = UserThingMapping.user_id
            JOIN Thing ON UserThingMapping.thing_id = Thing.id
            WHERE Thing.type = {filter_type}
        """.format(
                filter_type=filter_type
            )
        )

    if filter_type >=0:
        if next_page:
            paginated_user_query = (
                paginated_user_query
                + """
            AND deleted=false AND (created < '{created}' OR (created = '{created}' AND id < '{last_id}'))
            ORDER BY created DESC, id DESC LIMIT {page_size}
            )
            """.format(
                    created=created, page_size=page_size, last_id=last_id
                )
            )
            order_query = "ORDER BY PaginatedAppUser.created DESC, PaginatedAppUser.id DESC;"
        else:
            paginated_user_query = (
                paginated_user_query
                + """
            AND deleted=false AND (created > '{created}' OR (created = '{created}' AND id > '{last_id}'))
            ORDER BY created, id LIMIT {page_size}
            )
            """.format(
                    created=created, page_size=page_size, last_id=last_id
                )
            )
            order_query = "ORDER BY PaginatedAppUser.created, PaginatedAppUser.id;"
    else:
        if next_page:
            paginated_user_query = (
                paginated_user_query
                + """
            WHERE deleted=false AND (created < '{created}' OR (created = '{created}' AND id < '{last_id}'))
            ORDER BY created DESC, id DESC LIMIT {page_size}
            )
            """.format(
                    created=created, page_size=page_size, last_id=last_id
                )
            )
            order_query = "ORDER BY PaginatedAppUser.created DESC, PaginatedAppUser.id DESC;"
        else:
            paginated_user_query = (
                paginated_user_query
                + """
            WHERE deleted=false AND (created > '{created}' OR (created = '{created}' AND id > '{last_id}'))
            ORDER BY created, id LIMIT {page_size}
            )
            """.format(
                    created=created, page_size=page_size, last_id=last_id
                )
            )
            order_query = "ORDER BY PaginatedAppUser.created, PaginatedAppUser.id;"

    query = (
        paginated_user_query
        + """
        SELECT PaginatedAppUser.id, PaginatedAppUser.name, PaginatedAppUser.countrycode, PaginatedAppUser.created,
        PaginatedAppUser.deleted, PaginatedAppUser.config, PaginatedAppUser.tuya_user_id,
        AppUserAuth.auth_id as auth_id, AppUserAuth.verified as verified FROM PaginatedAppUser
        INNER JOIN AppUserAuth ON AppUserAuth.user_id = PaginatedAppUser.id 
    """
        + order_query
    )

    # cursor.execute(query)
    # results = cursor.fetchall()
    # cursor.close()
    # if not results:
    #     return ([], None)

    # last_row = results[len(results) - 1]
    # cursor_string = str(last_row["created"].timestamp()) + ":" + last_row["id"]
    # page_cursor = base64.b64encode(cursor_string.encode("utf-8")).decode("utf-8")
    return query, page_cursor


print(get_paginated_app_user()[0])