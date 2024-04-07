
# SNOWFLAKE ADVANTAGE: Python Stored Procedures

# snow snowpark build
# snow snowpark deploy --replace

import time
from snowflake.snowpark import Session
#import snowflake.snowpark.types as T
import snowflake.snowpark.functions as F


def main(session: Session) -> str:

    # returns list
    result = session.sql("SELECT CURRENT_USER();").collect()

    # return "Hello World! " + session.get_current_user()

    return "Hello World! " + str(result)


# For local debugging
# Be aware you may need to type-convert arguments if you add input parameters
if __name__ == '__main__':
    # Create a local Snowpark session
    with Session.builder.getOrCreate() as session:
        import sys
        if len(sys.argv) > 1:
            print(main(session, *sys.argv[1:]))  # type: ignore
        else:
            print(main(session))  # type: ignore
