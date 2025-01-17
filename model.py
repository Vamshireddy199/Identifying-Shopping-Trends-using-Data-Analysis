import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('/content/shopping_trends.csv')
print(data.head())
print(data.info())

plt.figure(figsize=(8, 5))
sns.histplot(data['Age'], kde=True, bins=20, color='blue')
plt.title("Distribution of Customer Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

avg_purchase_by_category = data.groupby('Category')['Purchase Amount (USD)'].mean()
print(avg_purchase_by_category)
avg_purchase_by_category.plot(kind='bar', figsize=(10, 5), color='orange')
plt.title("Average Purchase Amount by Category")
plt.xlabel("Category")
plt.ylabel("Average Purchase Amount (USD)")
plt.show()

gender_purchases = data['Gender'].value_counts()
print(gender_purchases)
gender_purchases.plot(kind='bar', color=['pink', 'blue'])
plt.title("Number of Purchases by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Purchases")
plt.show()

most_purchased_items = data.groupby('Category')['Item Purchased'].agg(lambda x: x.value_counts().idxmax())
print(most_purchased_items)

seasonal_spending = data.groupby('Season')['Purchase Amount (USD)'].sum()
seasonal_spending.plot(kind='bar', figsize=(10, 5), color='green')
plt.title("Customer Spending by Season")
plt.xlabel("Season")
plt.ylabel("Total Spending (USD)")
plt.show()

avg_rating_by_category = data.groupby('Category')['Review Rating'].mean()
print(avg_rating_by_category)
avg_rating_by_category.plot(kind='bar', figsize=(10, 5), color='purple')
plt.title("Average Rating by Category")
plt.xlabel("Category")
plt.ylabel("Average Rating")
plt.show()

subscribed_behavior = data.groupby('Subscription Status')['Purchase Amount (USD)'].mean()
print(subscribed_behavior)

payment_methods = data['Payment Method'].value_counts()
print(payment_methods)
payment_methods.plot(kind='bar', figsize=(8, 5), color='cyan')
plt.title("Most Popular Payment Methods")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.show()

promo_code_spending = data.groupby('Promo Code Used')['Purchase Amount (USD)'].mean()
print(promo_code_spending)

age_groups = pd.cut(data['Age'], bins=[0, 18, 30, 50, 70, 100], labels=['0-18', '19-30', '31-50', '51-70', '71+'])
age_group_purchases = data.groupby(age_groups)['Customer ID'].count()
print(age_group_purchases)
age_group_purchases.plot(kind='bar', figsize=(8, 5), color='teal')
plt.title("Purchase Frequency by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Purchases")
plt.show()

correlation = data[['Size', 'Purchase Amount (USD)']].corr(numeric_only=True)
print(correlation)
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Between Size and Purchase Amount")
plt.show()

preferred_shipping = data.groupby('Category')['Shipping Type'].agg(lambda x: x.value_counts().idxmax())
print(preferred_shipping)

discount_effect = data.groupby('Discount Applied')['Purchase Amount (USD)'].mean()
print(discount_effect)

popular_colors = data['Color'].value_counts()
print(popular_colors.head())
popular_colors.head(10).plot(kind='bar', figsize=(8, 5), color='violet')
plt.title("Most Popular Colors")
plt.xlabel("Color")
plt.ylabel("Count")
plt.show()

avg_previous_purchases = data['Previous Purchases'].mean()
print("Average Number of Previous Purchases:", avg_previous_purchases)

purchase_by_rating = data.groupby('Review Rating')['Purchase Amount (USD)'].mean()
print(purchase_by_rating)
purchase_by_rating.plot(kind='bar', figsize=(8, 5), color='magenta')
plt.title("Purchase Amount by Review Ratings")
plt.xlabel("Review Rating")
plt.ylabel("Average Purchase Amount (USD)")
plt.show()

location_behavior = data.groupby('Location')['Purchase Amount (USD)'].mean()
print(location_behavior)
location_behavior.plot(kind='bar', figsize=(12, 6), color='orange')
plt.title("Purchase Behavior by Location")
plt.xlabel("Location")
plt.ylabel("Average Purchase Amount (USD)")
plt.show()

age_category = data.groupby('Category')['Age'].mean()
print(age_category)

gender_spending = data.groupby('Gender')['Purchase Amount (USD)'].mean()
print(gender_spending)
gender_spending.plot(kind='bar', figsize=(8, 5), color=['pink', 'blue'])
plt.title("Purchase Amount by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Purchase Amount (USD)")
plt.show()
