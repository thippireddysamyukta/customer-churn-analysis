import pandas as pd

# Step 1: Create dataset
data = {
    "customer_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "months_stayed": [2, 24, 1, 36, 3, 18, 1, 12, 2, 48],
    "login_frequency": [1, 15, 0, 20, 1, 12, 0, 10, 2, 25],
    "support_contacts": [5, 1, 8, 0, 6, 2, 7, 1, 5, 0],
    "last_login_days_ago": [20, 2, 30, 1, 25, 5, 14, 3, 18, 1],
    "churned": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
print(df)

# Step 2: Compare churned vs active
print(df.groupby("churned").mean().round(2))

# Step 3: Flag at-risk customers
df["at_risk"] = ((df["last_login_days_ago"] >= 14) &
                 (df["support_contacts"] >= 3)).astype(int)
print(df[["customer_id", "last_login_days_ago", "support_contacts", "at_risk", "churned"]])

# Step 4: Summary
df.to_csv("churn_analysis.csv", index=False)
churned = df[df["churned"] == 1]
print("=== CHURN ANALYSIS SUMMARY ===")
print(f"Total customers: {len(df)}")
print(f"Churned customers: {len(churned)}")
print(f"Churn rate: {len(churned)/len(df)*100}%")
print("\nKey reasons for churn:")
print("1. No login for 14+ days")
print("2. High support contacts (3+)")
print("3. Low login frequency")
print("\nRetention suggestions:")
print("1. Send re-engagement email after 7 days of no login")
print("2. Proactively help customers with 3+ support tickets")
print("3. Offer loyalty rewards for frequent logins")
