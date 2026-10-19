import numpy as np
import pandas as pd

# Read Dataset
data = pd.read_csv("MiniProjects/sales_data.csv")

# Extract Columns
order_id = data["order_id"].to_numpy()
quantity = data["quantity"].to_numpy()
price = data["price"].to_numpy()
discount = data["discount"].to_numpy()
customer_age = data["customer_age"].to_numpy()
rating = data["rating"].to_numpy()


class SalesAnalyzer:

    # 1. Total Revenue
    @staticmethod
    def TotalRevenue():
        revenue = quantity * price
        final_revenue = revenue - (revenue * discount / 100)

        print("Total Revenue:", np.sum(final_revenue))

    # 2. Average Order Value
    @staticmethod
    def AvgOrderValue():
        revenue = quantity * price
        final_revenue = revenue - (revenue * discount / 100)

        print("Average Order Value:", np.mean(final_revenue))

    # 3. Highest Revenue Order
    @staticmethod
    def HighestRevenueOrder():
        revenue = quantity * price
        final_revenue = revenue - (revenue * discount / 100)

        index = np.argmax(final_revenue)

        print("Order ID:", order_id[index])
        print("Highest Revenue:", final_revenue[index])

    # 4. Lowest Revenue Order
    @staticmethod
    def LowestRevenueOrder():
        revenue = quantity * price
        final_revenue = revenue - (revenue * discount / 100)

        index = np.argmin(final_revenue)

        print("Order ID:", order_id[index])
        print("Lowest Revenue:", final_revenue[index])

    # 5. Total Quantity Sold
    @staticmethod
    def TotalQuantitySold():
        print("Total Quantity Sold:", np.sum(quantity))

    # 6. Average Discount
    @staticmethod
    def AverageDiscount():
        print("Average Discount:", np.mean(discount), "%")

    # 7. Average Customer Age
    @staticmethod
    def AverageCustomerAge():
        print("Average Customer Age:", np.mean(customer_age))

    # 8. Correlation Between Rating and Revenue
    @staticmethod
    def RatingRevenueCorrelation():
        revenue = quantity * price
        final_revenue = revenue - (revenue * discount / 100)

        correlation = np.corrcoef(rating, final_revenue)[0, 1]

        print("Rating-Revenue Correlation:", correlation)

    # 9. Detect Unusual Orders Using IQR
    @staticmethod
    def DetectUnusualOrders():
        revenue = quantity * price
        final_revenue = revenue - (revenue * discount / 100)

        q1 = np.percentile(final_revenue, 25)
        q3 = np.percentile(final_revenue, 75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        unusual = (final_revenue < lower) | (final_revenue > upper)

        print("Unusual Order IDs:", order_id[unusual])

    # 10. Normalize Revenue
    @staticmethod
    def NormalizeRevenue():
        revenue = quantity * price
        final_revenue = revenue - (revenue * discount / 100)

        normalized = (
            (final_revenue - np.min(final_revenue)) /
            (np.max(final_revenue) - np.min(final_revenue))
        )

        print("Normalized Revenue:", np.round(normalized, 3))

    # 11. Find Top 5 Orders
    @staticmethod
    def Top5Orders():
        revenue = quantity * price
        final_revenue = revenue - (revenue * discount / 100)

        indices = np.argsort(final_revenue)[::-1][:5]

        print("Top 5 Orders:")

        for i in indices:
            print(
                "Order ID:", order_id[i],
                "| Final Revenue:", final_revenue[i]
            )

    # 12. Categorize Customers by Age
    @staticmethod
    def CategorizeCustomersByAge():
        conditions = [
            customer_age < 30,
            (customer_age >= 30) & (customer_age < 45),
            customer_age >= 45
        ]

        categories = ["Young", "Adult", "Senior"]

        age_category = np.select(
            conditions,
            categories,
            default="Unknown"
        )

        for i in range(len(order_id)):
            print(
                "Order ID:", order_id[i],
                "| Age:", customer_age[i],
                "| Category:", age_category[i]
            )




print("========== SALES ANALYZER ==========")
while True:

    print("\n1. Total Revenue")
    print("2. Average Order Value")
    print("3. Highest Revenue Order")
    print("4. Lowest Revenue Order")
    print("5. Total Quantity Sold")
    print("6. Average Discount")
    print("7. Average Customer Age")
    print("8. Rating-Revenue Correlation")
    print("9. Detect Unusual Orders")
    print("10. Normalize Revenue")
    print("11. Top 5 Orders")
    print("12. Categorize Customers by Age")
    print("0. Exit")

    try:
        n = int(input("Enter Your Command: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    match n:

        case 1:
            SalesAnalyzer.TotalRevenue()

        case 2:
            SalesAnalyzer.AvgOrderValue()

        case 3:
            SalesAnalyzer.HighestRevenueOrder()

        case 4:
            SalesAnalyzer.LowestRevenueOrder()

        case 5:
            SalesAnalyzer.TotalQuantitySold()

        case 6:
            SalesAnalyzer.AverageDiscount()

        case 7:
            SalesAnalyzer.AverageCustomerAge()

        case 8:
            SalesAnalyzer.RatingRevenueCorrelation()

        case 9:
            SalesAnalyzer.DetectUnusualOrders()

        case 10:
            SalesAnalyzer.NormalizeRevenue()

        case 11:
            SalesAnalyzer.Top5Orders()

        case 12:
            SalesAnalyzer.CategorizeCustomersByAge()

        case 0:
            print("Thank you for using Sales Analyzer!")
            break

        case _:
            print("Invalid choice! Enter a number from 0 to 12.")

