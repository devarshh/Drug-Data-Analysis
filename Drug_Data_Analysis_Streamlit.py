import streamlit as st

st.markdown("# Exploratory Data Analysis (EDA) of National Drug Seizures FY 21-24")

st.markdown("## Devarsh Vanditkumar Joshi")
st.markdown("### B.Sc. Hons. Computer Science Co-op student @ Ontario Tech University")
st.markdown("Drug trafficking poses a grave threat to public safety and national security. Analyzing drug seizure data provides an opportunity to identify geographical patterns, understand trafficking methods, and evaluate the effectiveness of law enforcement. This project delves into the Nationwide Drug Seizures dataset to extract actionable insights and inform strategies for combating this menace.")

st.markdown("---")

st.markdown("## Objectives")

st.markdown("1. **Identify Regional Trends**:")
st.markdown("- Pinpoint regions with heightened drug-related activity.")
st.markdown("- Determine the most prevalent drug categories within these regions.")

st.markdown("2. **Examine Temporal Patterns**:")
st.markdown("- Analyze seasonal and annual trends in drug seizure incidents and quantities.")
st.markdown("- Identify peak periods of activity to refine enforcement approaches.")

st.markdown("3. **Evaluate Trafficking Methods**:")
st.markdown("- Investigate seizure patterns based on trafficking modes, including land, air, and sea.")

st.markdown("---")

st.markdown("## Approach")

st.markdown("Using Python-based data analysis tools, this project will examine the dataset through:")
st.markdown("- **Data Cleaning**: Ensuring the dataset is free from inconsistencies and missing values.")
st.markdown("- **Visualizations**: Using advanced visualizations to uncover patterns.")

st.markdown("---")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as animation
import numpy as np


plt.style.use('dark_background')
data = pd.read_csv('nationwide-drugs-fy21-fy24.csv')

data.rename(columns={'Sum Qty (lbs)': 'Weight (lbs)'}, inplace=True)
data['Land Filter'] = data['Land Filter'].str.strip().str.upper()

head_display = data.head(10)
head_display

st.markdown("---")

st.markdown("## Dataset Description")

st.markdown("The dataset includes detailed information about drug seizures across various regions in the United States. Key attributes of the dataset are as follows:")

st.markdown("- **Region**: The geographical area where the event occurred.")
st.markdown("- **Drug Type**: The type of drug involved in the seizure.")
st.markdown("- **Count of Event**: The number of incidents or seizures recorded for a specific drug type.")
st.markdown("- **Sum Qty (lbs)**: The total weight of drugs seized, measured in pounds.")
st.markdown("- **Land Filter**: Indicates the mode of trafficking.")
st.markdown("- **Component**: The enforcement agency responsible for the seizure.")

st.markdown("### Observations:")
st.markdown("- The dataset spans multiple years and includes detailed records, enabling temporal and regional analyses.")
st.markdown("- Drug types show significant variation in quantity and frequency across regions.")
st.markdown("- The dataset provides a strong foundation for understanding trafficking patterns and enforcement effectiveness.")

st.markdown("---")

st.markdown("### Total Weight by Drug Type")
total_weight_by_drug = data.groupby('Drug Type')['Weight (lbs)'].sum()


plt.figure(figsize=(12, 6))
total_weight_by_drug.sort_values(ascending=False).plot(kind='bar', color='sandybrown', zorder=2)
plt.title('Total Weight by Drug Type', fontsize=14, fontweight='bold', color='lime')
plt.xlabel('Drug Type', fontsize=12)
plt.ylabel('Total Weight (lbs)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=1)
st.pyplot(plt.gcf())

st.markdown("---")

st.markdown("The bar chart above illustrates the total weight of different drug types seized, measured in pounds. The analysis reveals the following key insights:")

st.markdown("**Questions Addressed**:")
st.markdown("1. Which drugs are most prevalent by weight?")
st.markdown("2. How does the distribution of synthetic drugs compare to traditional ones?")

st.markdown("### Key Observations:")
st.markdown("1. **Marijuana** dominates the dataset, accounting for the highest weight among all drug types, far exceeding others.")
st.markdown("2. **Methamphetamine** and **Khat (Catha Edulis)** also contribute significantly to the total weight, indicating their prevalence in drug trafficking activities.")
st.markdown("3. **Cocaine** follows as another prominent drug type, although its total weight is considerably lower than the top three.")
st.markdown("4. Other drugs, including **Fentanyl**, **Ketamine**, and **Heroin**, have much lower quantities in comparison but are still critical due to their potency and impact.")

st.markdown("### Insights:")
st.markdown("- **Marijuana**'s overwhelming dominance highlights its widespread nature in trafficking and seizures.")
st.markdown("- The presence of synthetic drugs like **Methamphetamine** and **Fentanyl** indicates the evolving nature of drug production and distribution.")

st.markdown("---")

st.markdown("### Regional Trends for Top 5 Drugs")
top_5_drugs = total_weight_by_drug.nlargest(5).index
region_drug_trends = data.groupby(['Region', 'Drug Type'])['Weight (lbs)'].sum().unstack()

region_drug_trends_top5 = region_drug_trends[top_5_drugs]

# Plotting
region_drug_trends_top5.plot(kind='bar', figsize=(14, 8), colormap='YlOrRd', zorder=2)
plt.title('Total Weight of Top 5 Drugs by Region', fontsize=14, fontweight='bold', color='lime')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Total Weight (lbs)', fontsize=12)
plt.legend(title='Drug Type', fontsize=10)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=1)
st.pyplot(plt.gcf())

st.markdown("---")

st.markdown("The bar chart above illustrates the total weight (in pounds) of the top 5 drugs seized across different regions. Each bar represents a drug type within a specific region, providing insights into the geographical distribution of drug seizures.")

st.markdown("### Questions Answered:")
st.markdown("1. How does the contribution of specific drugs vary across regions?")
st.markdown("2. Are there significant differences in drug types across regions?")
st.markdown("3. Are there specific drugs that should be prioritized for enforcement in certain regions?")

st.markdown("### Key Observations:")
st.markdown("1. **Coastal/Interior Region**:")
st.markdown("   - This region shows the highest total weight across all drug types, with **Khat (Catha Edulis)** and **Cocaine** contributing significantly.")
st.markdown("   - **Marijuana** also forms a substantial part of the seizures in this region.")

st.markdown("2. **Northern Border**:")
st.markdown("   - **Marijuana** dominates the seizures in this region, with relatively smaller contributions from other drug types.")

st.markdown("3. **Southwest Border**:")
st.markdown("   - **Methamphetamine** leads the drug seizures in this region, followed by Marijuana.")
st.markdown("   - Other drugs such as Cocaine and Khat are less prominent here.")

st.markdown("### Insights:")
st.markdown("- The **Coastal/Interior** region has a diverse and high-volume distribution of drug types, indicating it as a critical area for trafficking activities.")
st.markdown("- **Methamphetamine** dominates in the **Southwest Border**, suggesting a focus on synthetic drug trafficking in this area.")
st.markdown("- **Marijuana** remains a consistent and significant contributor across all regions.")

st.markdown("---")

st.markdown("### Monthly Trends in Top 3 Drug Types by Weight")

top_3_drugs = total_weight_by_drug.nlargest(3).index
region_drug_trends = data.groupby(['Region', 'Drug Type'])['Weight (lbs)'].sum().unstack()

month_order = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
drug_trends = data.groupby(['Month (abbv)', 'Drug Type'])['Weight (lbs)'].sum().unstack()
drug_trends = drug_trends.reindex(month_order)

# Plotting
drug_trends[top_3_drugs].plot(figsize=(12, 8), marker='o', colormap='YlOrRd')
plt.title('Monthly Trends in Top 3 Drug Types by Weight', fontsize=14, fontweight='bold', color='lime')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Weight (lbs)', fontsize=12)
plt.legend(title='Drug Type', fontsize=10)
plt.grid(axis='both', linestyle='--', alpha=0.0)
plt.xticks(rotation=45)
st.pyplot(plt.gcf())

st.markdown("The line chart above displays the monthly trends in the total weight (in pounds) of the top 3 drug types seized. This visualization helps in understanding the temporal patterns for the most significant drug types.")

st.markdown("### Questions Answered:")
st.markdown("1. Are there specific months with consistently high activity for any of the top 3 drugs?")
st.markdown("2. Do the trends indicate any emerging or declining popularity of specific drugs over the months?")
st.markdown("3. Can these monthly trends guide enforcement agencies in planning resource allocation for high-activity periods?")

st.markdown("### Key Observations:")
st.markdown("1. **Marijuana**:")
st.markdown("   - Consistently shows high weights throughout the year, with noticeable peaks in specific months.")
st.markdown("   - Suggests consistent trafficking activity with periodic spikes.")

st.markdown("2. **Methamphetamine**:")
st.markdown("   - Exhibits more fluctuation compared to **Marijuana**, with significant peaks and drops across the months.")
st.markdown("   - Indicates seasonality or specific operational patterns in trafficking.")

st.markdown("3. **Khat (Catha Edulis)**:")
st.markdown("   - Displays irregular patterns with occasional spikes, suggesting occasional trafficking events rather than steady activity.")

st.markdown("### Insights:")
st.markdown("- The temporal trends highlight the need for region-specific and time-sensitive enforcement measures.")
st.markdown("- Spikes in specific months can help law enforcement focus their resources during high-activity periods for certain drugs.")
st.markdown("- The fluctuation in Methamphetamine and Khat activities may correspond to changes in supply chains or enforcement effectiveness.")

st.markdown("---")

st.markdown("### Monthly Trends in Top 3 Drug Types by Events per year")

filtered_data_no_other = data[data['Drug Type'] != 'Other Drugs**']
top_3_drugs_per_year = (
   filtered_data_no_other.groupby(['FY', 'Drug Type'])['Count of Event']
   .sum()
   .reset_index()
   .sort_values(by=['FY', 'Count of Event'], ascending=[True, False])
)

# Create a dictionary of top 3 drugs per year
top_3_per_year = (
   top_3_drugs_per_year.groupby('FY')['Drug Type']
   .apply(lambda x: x.head(3).tolist())
   .to_dict()
)

# Generate plots for each year
unique_years = sorted(filtered_data_no_other['FY'].unique())

for year in unique_years:
   # Filter data for the year and top 3 drugs
   year_top_3_drugs = top_3_per_year[year]
   year_data = filtered_data_no_other[
      (filtered_data_no_other['FY'] == year) & (filtered_data_no_other['Drug Type'].isin(year_top_3_drugs))
      ]

   # Aggregating monthly data for the top 3 drugs
   monthly_data = year_data.groupby(['Month (abbv)', 'Drug Type'])['Count of Event'].sum().reset_index()

   # Pivot data for plotting
   monthly_pivot = monthly_data.pivot_table(
      index='Month (abbv)', columns='Drug Type', values='Count of Event', fill_value=0
   )

   # Sorting months for proper order
   monthly_pivot = monthly_pivot.reindex(month_order)

   # Plotting the data
   ax = monthly_pivot.plot(kind='line', figsize=(12, 6), zorder=2)

   for drug in year_top_3_drugs:
      if drug in monthly_pivot.columns:
         peak_month = monthly_pivot[drug].idxmax()
         peak_value = monthly_pivot[drug].max()
         peak_index = month_order.index(peak_month)
         ax.plot(peak_index, peak_value, marker='v', color='sandybrown', markersize=8)
         ax.text(
            peak_index, peak_value + 25, 'Peak', fontsize=9, color='sandybrown', ha='center'
         )

   plt.title(f'Monthly Trends for Top 3 Drugs in {year}', fontsize=14, fontweight='bold', color='lime')
   plt.xlabel('Month')
   plt.ylabel('Number of Events')
   plt.xticks(rotation=45)
   plt.legend(title='Drug Type', bbox_to_anchor=(1.05, 1), loc='upper left')
   plt.tight_layout()
   plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=1)
   plt.grid(axis='x', linestyle='--', alpha=0.7, zorder=1)
   st.pyplot(plt.gcf())

st.markdown("---")

st.markdown("This visualization analyzes the monthly trends in the top 3 drug types for each year based on the number of events. We approached to events, as although we considered the weight analsis, it cannot be trusted as some synthetic drugs which weigh less, can be as bad of a problem as traditional drugs. The chart displays separate lines for each drug type, showing how their activity fluctuates over the months.")

st.markdown("### Questions Answered")
st.markdown("1. Are there discernible patterns that indicate emerging or declining trafficking trends for specific drugs?")
st.markdown("2. Do the trends indicate any emerging or declining popularity of specific drugs over the years?")
st.markdown("3. Can this data aid enforcement agencies in identifying peak periods for focused intervention?")

st.markdown("### Key Observations:")
st.markdown("1. **Drug-Specific Observations**:")
st.markdown("   - **Marijuana**:")
st.markdown("     - Maintains a strong presence throughout the years with notable peaks, such as March in 2021 and July in 2024.")
st.markdown("   - **Methamphetamine**:")
st.markdown("     - Exhibits fluctuating patterns with prominent spikes, suggesting operational bursts in its trafficking supply chain.")
st.markdown("   - **Cocaine**:")
st.markdown("     - While less dominant, **Cocaine** displays a steady presence, with sporadic peaks indicating targeted trafficking efforts.")

st.markdown("2.  **Fluctuations in Seizures**:")
st.markdown("   - The varying patterns across months and years suggest adaptive strategies employed by traffickers to evade detection or capitalize on specific market demands.")

st.markdown("### Insights:")
st.markdown("- **Marijuana** consistently appears as a dominant drug type across all years, reflecting its persistent trafficking trends.")
st.markdown("- Each year demonstrates distinct patterns for event counts, indicating potential shifts in trafficking trends or enforcement priorities.")
st.markdown("- **Methamphetamine** shows significant peaks in September for certain years, which may indicate seasonal trafficking trends or enforcement spikes.")

st.markdown("---")

st.markdown("### Share of Each Drug Types over Time")

#Preparing data
time_series = data.groupby(['FY', 'Month (abbv)', 'Drug Type'])[['Count of Event']].sum().reset_index()

area_chart_data = time_series.pivot_table(index=['FY', 'Month (abbv)'], columns='Drug Type', values='Count of Event', aggfunc='sum', fill_value=0).reset_index()

# Aggregating data for visualization
area_chart_data['Month-Year'] = area_chart_data['FY'].astype(str) + " " + area_chart_data['Month (abbv)']
area_chart_data = area_chart_data.drop(columns=['FY', 'Month (abbv)']).set_index('Month-Year')

# Stacked area chart
area_chart_data.plot(kind='area', figsize=(14, 8), stacked=True, colormap='tab10', zorder=2)
plt.title('Share of Drug Types Over Time', fontsize=14, fontweight='bold', color='lime')
plt.xlabel('Month-Year')
plt.ylabel('Number of Events')
plt.xticks(rotation=45)
plt.legend(title='Drug Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=1)
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("---")

st.markdown("The stacked area chart above represents the share of different drug types over time, measured by the number of events in each month-year. The visualization provides insights into how the distribution of drug types has evolved over time.")

st.markdown("### Questions Answered:")
st.markdown("1. How does the volume of seizures for specific drug types fluctuate within the observed timeframe?")
st.markdown("2. Are there any noticeable trends or consistent patterns in the share of specific drugs over the months and years?")
st.markdown("3. Which drug types consistently dominate the share of seizures?")

st.markdown("### Key Observations:")
st.markdown("1. **Marijuana**:")
st.markdown("   - Consistently contributes the largest share of events over time, with fluctuations indicating possible changes in trafficking activity.")
st.markdown("2. **Other Drugs**:")
st.markdown("- This category forms a significant proportion of the events, highlighting the diversity of lesser-known drug types.")
st.markdown("3. **Methamphetamine and Cocaine**:")
st.markdown("- These drugs show noticeable activity, with **Methamphetamine** maintaining a consistent presence.")
st.markdown("4. **Emerging Trends**:")
st.markdown("- Drugs like **Fentanyl** and **Khat (Catha Edulis)** show irregular but increasing trends, indicating their growing importance.")

st.markdown("### Insights:")
st.markdown("- The dominance of **Marijuana** suggests it remains a primary focus for enforcement efforts.")
st.markdown("- The relative stability of certain drugs like **Methamphetamine** contrasts with the fluctuating presence of others, hinting at differences in supply chains or enforcement success.")
st.markdown("- The temporal trends help in identifying months or periods with spikes, allowing for targeted interventions.")

st.markdown("---")


st.markdown("### Stacked Bar Chart: Events by Drug Type for Top 10 Areas")
data['Area'] = data['Area of Responsibility'].str.replace(" FIELD OFFICE", "", regex=False)

treemap_data = data.groupby(['Area', 'Drug Type'])['Count of Event'].sum().reset_index()


# Constructing labels for the treemap
treemap_data['Label'] = (
    treemap_data['Area'] + "\n" + treemap_data['Drug Type'] + "\n" +
    treemap_data['Count of Event'].astype(str) + " events"
)


top_aors = treemap_data.groupby('Area')['Count of Event'].sum().nlargest(10).index
top_aors_data = treemap_data[treemap_data['Area'].isin(top_aors)]

pivot_data = top_aors_data.pivot_table(
    index='Area',
    columns='Drug Type',
    values='Count of Event',
    aggfunc='sum',
    fill_value=0
)

# Visualizing the treemap using a bar chart alternative
pivot_data.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='tab10', zorder=2)
plt.title('Stacked Bar Chart: Events by Drug Type for Top 10 Areas', fontsize=14, fontweight='bold', color='lime')
plt.xlabel('Area')
plt.ylabel('Number of Events')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Drug Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=1)
st.pyplot(plt.gcf())

st.markdown("---")

st.markdown("The stacked bar chart above showcases the distribution of drug-related events across the top 10 areas of responsibility. Each bar represents the total number of events in a specific area, broken down by drug type.")

st.markdown("### Questions Answered:")
st.markdown("1. Are specific areas dominated by certain drug types, indicating localized trafficking patterns?")
st.markdown("2. Do larger metropolitan areas show a higher diversity of drug types compared to smaller cities?")
st.markdown("3. What insights can be drawn regarding the consistency or variability of drug presence across the top regions?")

st.markdown("### Key Observations:")
st.markdown("1. **New York**:")
st.markdown("   - This area has the highest number of drug-related events, with a significant contribution from **Other Drugs** and **Marijuana**.")
st.markdown("2. **Chicago and Miami**:")
st.markdown("   - These areas also show high levels of activity, with **Methamphetamine** and **Cocaine** contributing prominently.")
st.markdown("3. **Regional Trends**:")
st.markdown("   - Some areas, like **San Francisco** and **Seattle**, show a more evenly distributed mix of drug types, indicating diverse trafficking patterns.")

st.markdown("### Insights:")
st.markdown("- The dominance of certain areas like **New York** and **Chicago** suggests these are critical hotspots for drug-related activities.")
st.markdown("- The variation in drug type contributions across areas indicates that trafficking strategies and enforcement challenges vary geographically.")
st.markdown("- Targeted enforcement efforts in the highlighted areas could significantly reduce the overall impact of drug trafficking.")

st.markdown("---")

st.markdown("### Regional Distribution of Events by Land Filter")
regional_land_filter = data.groupby(['Region', 'Land Filter'])['Count of Event'].sum().unstack(fill_value=0)

# Plotting a stacked bar chart for events by region and land filter
regional_land_filter.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='YlOrRd', zorder=2)
plt.title('Regional Distribution of Events by Land Filter', fontsize=14, fontweight='bold', color='lime')
plt.xlabel('Region')
plt.ylabel('Number of Events')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Land Filter', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='both', linestyle='--', alpha=0.7, zorder=1)
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("---")
st.markdown("The bar chart above illustrates the regional distribution of drug-related events, categorized by the **Land Filter** variable, which identifies whether the seizure occurred via land or other methods.")

st.markdown("### Questions Answered:")
st.markdown("1. Which regions have the highest number of drug events?")
st.markdown("2. Does the high volume of events in the Coastal/Interior region suggest gaps in monitoring non-land-based methods?")
st.markdown("3. Are certain regions more reliant on land-based trafficking compared to others?")

st.markdown("### Key Observations:")
st.markdown("1. **Coastal/Interior Region**:")
st.markdown("- This region dominates the chart, with the majority of events categorized as **OTHER**.")
st.markdown("- Indicates significant activity involving non-land-based trafficking methods.")
st.markdown("2. **Southwest Border**:")
st.markdown("- This region has the highest number of **LAND ONLY** events, suggesting land is the predominant mode of trafficking.")
st.markdown("3. **Northern Border**:")
st.markdown("- Exhibits relatively low event counts compared to other regions, with a mix of both land and other modes.")

st.markdown("### Insights:")
st.markdown("- The **Coastal/Interior region's dominance** in \"OTHER\" events highlights its role as a key trafficking hub for non-land methods.")
st.markdown("- The **Southwest Border** is heavily reliant on land routes, suggesting that enforcement efforts in this region should focus on land-based transportation methods.")
st.markdown("- Understanding these distributions helps prioritize resources for specific regions and trafficking modes, enabling more efficient and targeted interventions.")

st.markdown("---")

st.markdown("### Regional Contribution of Events by Component")
regional_component_data = data.groupby(['Region', 'Component'])['Count of Event'].sum().unstack(fill_value=0)

# Plotting a heatmap for regional contributions by component
plt.figure(figsize=(12, 8))
sns.heatmap(regional_component_data, annot=True, fmt="d", cmap="YlOrRd", linewidths=0.5, linecolor='black')
plt.title('Regional Contribution of Events by Component', fontsize=14, fontweight='bold', color='lime')
plt.xlabel('Component')
plt.ylabel('Region')
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("The heatmap above visualizes the contribution of different components to drug-related events across various regions. The **Office of Field Operations** and **U.S. Border Patrol** are the two primary components contributing to the event counts.")

st.markdown("### Questions Answered:")
st.markdown("1. Which regions are predominantly handled by each enforcement component?")
st.markdown("2. How do different regions contribute to the volume of drug-related events for each enforcement component?")
st.markdown("3. Does the low activity in certain regions suggest gaps in operations by either of the components?")

st.markdown("### Observations:")
st.markdown("1. **Coastal/Interior Region**:")
st.markdown("- The **Office of Field Operations** dominates, contributing the highest number of events (190,955), with minimal input from the **U.S. Border Patrol**.")
st.markdown("2. **Southwest Border**:")
st.markdown("- Both components contribute significantly, though the **Office of Field Operations** maintains a higher share.")
st.markdown("3. **Northern Border**:")
st.markdown("- The event count is relatively low compared to other regions, with a marginal contribution from the **U.S. Border Patrol**.")

st.markdown("### Insights:")
st.markdown("- The **Office of Field Operations** is the primary contributor across all regions, highlighting its critical role in enforcement activities.")
st.markdown("- The **Southwest Border** sees a more balanced contribution from both components, suggesting varied enforcement strategies.")
st.markdown("- The **Coastal/Interior region's** reliance on the **Office of Field Operations** suggests a focus on specific types of trafficking activities.")

st.markdown("---")

st.markdown("### Monthly Event Distribution on Polar Axis")

# Preparing data for a polar bar chart
monthly_events = data.groupby('Month (abbv)')['Count of Event'].sum().reindex(month_order)

angles = np.linspace(0, 2 * np.pi, len(month_order), endpoint=False).tolist()

# Plotting the bar chart on polar axis
plt.figure(figsize=(10, 8))
ax = plt.subplot(111, polar=True)

bars = ax.bar(
    angles, monthly_events, align='center', alpha=0.8, edgecolor="black",
    color=plt.cm.YlOrRd(np.linspace(0, 1, len(month_order)))
)

ax.set_xticks(angles)
ax.set_xticklabels(month_order, fontsize=10, fontweight='bold')
ax.yaxis.grid(color='white', linestyle='--', linewidth=0.7)
ax.spines['polar'].set_visible(False)
ax.tick_params(axis='y', colors='red')
ax.tick_params(axis='x', colors='black')
for label in ax.get_yticklabels():
    label.set_fontweight('bold')

for label in ax.get_xticklabels():
    label.set_bbox(dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.1'))


plt.title('Monthly Event Distribution on Polar Axis', va='bottom', fontsize=14, fontweight='bold', color='lime')
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("---")

st.markdown("The polar bar chart above visualizes the distribution of drug-related events across months, providing a unique perspective on temporal trends.")

st.markdown("### Questions Answered:")
st.markdown("1. Are there specific months with consistently higher event counts?")
st.markdown("2. Can this temporal distribution guide resource allocation for high-activity periods?")
st.markdown("3. Which months require intensified enforcement measures based on higher activity?")


st.markdown("### Key Observations:")
st.markdown("1. **Peak Months**:")
st.markdown("- The highest activity is observed in **January**, as indicated by the longest and darkest bar.")
st.markdown("2. **Seasonal Trends**:")
st.markdown("- Activity gradually reduces in the summer months (**June–August**) and picks up towards the end of the year (**November–December**).")
st.markdown("3. **Even Distribution**:")
st.markdown("- Although some months like **January** and **February** stand out, there is a relatively even spread of events throughout the year, indicating consistent trafficking activity.")

st.markdown("### Insights:")
st.markdown("- The polar chart provides a clear visual representation of temporal trends, making it easy to identify seasonal peaks and troughs.")
st.markdown("- Enforcement agencies can use this insight to allocate resources more effectively during high-activity months, especially at the start and end of the year.")
st.markdown("- The consistent activity suggests that trafficking is a year-round issue, requiring continuous monitoring.")

st.markdown("---")


st.markdown("### Summary Statistics")
summary_stats = data.describe()
summary_stats

st.markdown("---")

st.markdown("## Conclusion")

st.markdown("This project successfully conducted an in-depth Exploratory Data Analysis (EDA) on the Nationwide Drug Seizures dataset, uncovering key patterns, trends, and insights. The analysis focused on regional, temporal, and categorical distributions of drug-related events, providing valuable inputs for enforcement and policymaking.")

st.markdown("### Summary of Key Findings:")
st.markdown("1. **Regional Insights**:")
st.markdown("   - The **Coastal/Interior Region** consistently recorded the highest number of drug-related events, largely dominated by non-land-based trafficking methods.")
st.markdown("   - The **Southwest Border** showed significant land-based activity, highlighting its role in land trafficking.")

st.markdown("2. **Drug Type Trends**:")
st.markdown("   - **Marijuana** emerged as the most frequently seized drug across all regions and time periods.")
st.markdown("   - Synthetic drugs like **Methamphetamine** and emerging substances like **Fentanyl** demonstrated fluctuating but growing trends, indicating evolving trafficking dynamics.")

st.markdown("3. **Temporal Analysis**:")
st.markdown("   - Seasonal trends were evident, with peak activity observed in **January** and a decline during the summer months.")
st.markdown("   - The consistency of events across most months suggests that trafficking is not limited to specific periods but requires year-round enforcement efforts.")

st.markdown("4. **Land and Component Contribution**:")
st.markdown("   - The **Office of Field Operations** played a dominant role in enforcement activities across all regions, with the **U.S. Border Patrol** contributing significantly at the **Southwest Border**.")
st.markdown("   - Regional variations in trafficking modes were clearly highlighted, aiding in understanding the operational challenges faced by different enforcement agencies.")

st.markdown("---")

st.markdown("## References")

st.markdown("1. **Libraries Used**:")
st.markdown("   - **Pandas**: For data manipulation and cleaning. Documentation available at [Pandas Documentation](https://pandas.pydata.org/docs/).")
st.markdown("   - **Matplotlib/Seaborn**: For data visualization. Documentation available at [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) and [Seaborn Documentation](https://seaborn.pydata.org/).")
st.markdown("- **NumPy**: For numerical analysis. Documentation available at [NumPy Documentation](https://numpy.org/doc/).")

st.markdown("2. **Dataset Source**:")
st.markdown("- [Nationwide Drug Seizures Dataset](https://www.cbp.gov/document/stats/nationwide-drug-seizures)")
st.markdown("This dataset was used for exploratory data analysis and question-driven insights in this notebook.")

st.markdown("3. **Large Language Models (LLMs)**:")
st.markdown("- **ChatGPT** was used for generating text contributions to the notebook. The prompts used include:")
st.markdown("     - \"Web scrape some ideas to show how to start an introduction explaining the purpose of using the Nationwide Drug Seizures dataset.\"")
st.markdown("     - \"What are the best practices for a clean structure in a Jupyter Notebook, and how to beautify some parts of it.\"")
st.markdown("     - \"Best practices when conducting Exploratory Data Analysis on a .csv dataset.\"")

st.markdown("4. **Data Science Workflow Reference**:")
st.markdown("   - O’Neil, C., & Schutt, R. (2014). *Doing Data Science* (1st ed.). O'Reilly Media.")
st.markdown("     The data science workflow mentioned in the assignment was referenced during the project's development.")

st.markdown("5. **Online Resources**:")
st.markdown(
   "   - **Markdown Syntax Reference**: [GitHub Markdown Documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)")
st.markdown("     Used to structure and format Markdown sections effectively.")
st.markdown("   - **Python.org**: [Python Language Reference](https://docs.python.org/3/)")
st.markdown("     Official documentation for Python programming language features used in this project.")
