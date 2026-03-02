from config.db_config import get_connection
from utils.logger import log_info

def generate_sales_report():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(total_amount) FROM orders")
    total_sales = cursor.fetchone()[0] or 0

    cursor.execute("SELECT COUNT(*) FROM orders")
    total_orders = cursor.fetchone()[0]

    insert_query = """
    INSERT INTO reports (report_type, total_sales, total_orders)
    VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, ("Sales Summary", total_sales, total_orders))
    conn.commit()

    cursor.close()
    conn.close()

    log_info("Sales report generated")

    return {
        "total_sales": total_sales,
        "total_orders": total_orders
    }