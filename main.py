
from database_tools import query_heart_disease_db, query_cancer_db, query_diabetes_db
from web_search_tool import medical_web_search

def main():
    while True:
        user_query = input("Ask a medical question (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break

        # Simple keyword-based routing
        if any(keyword in user_query.lower() for keyword in ["statistics", "data", "average", "count", "how many"]):
            if "heart" in user_query.lower() or "hd" in user_query.lower():
                # A bit of a hack to form a query, a proper NL to SQL would be better
                sql_query = "SELECT * FROM heart_disease LIMIT 5;"
                print(query_heart_disease_db(sql_query))
            elif "cancer" in user_query.lower():
                sql_query = "SELECT * FROM cancer LIMIT 5;"
                print(query_cancer_db(sql_query))
            elif "diabetes" in user_query.lower():
                sql_query = "SELECT * FROM diabetes LIMIT 5;"
                print(query_diabetes_db(sql_query))
            else:
                print("Could not determine which database to query. Please be more specific.")
        else:
            print(medical_web_search(user_query))

if __name__ == '__main__':
    main()
