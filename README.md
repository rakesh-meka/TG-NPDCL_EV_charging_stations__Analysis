# TG-NPDCL EV Charging Stations Consumption Analysis

## 📌 Project Overview
This project analyzes **EV charging station consumption data** from the **Telangana Northern Power Distribution Company Limited (TG-NPDCL)** for the year **2024**. The data, obtained from public monthly reports, was processed using Python to extract insights on **electricity consumption, high and low-demand regions, and seasonal trends**.

## 📂 Dataset Information
## 🔗 Source
**Website**: [Telangana Open Data Portal](https://data.telangana.gov.in/)  
**Dataset Link**: [TG-NPDCL EV Charging Consumption Data](https://data.telangana.gov.in/dataset/tg-npdcl-ev-charging-stations-consumption-data)
This dataset has been downloaded from the [Telangana Open Data Portal](https://data.telangana.gov.in/dataset/tg-npdcl-ev-charging-stations-consumption-data). It contains information on electricity consumption at electric vehicle (EV) charging stations under **TG-NPDCL (Telangana Northern Power Distribution Company Limited)**.

The data consists of monthly, I have **merged monthly reports** from January 2024 to December 2024 using python.
The key columns include:
- **Circle, Division, Subdivision, Section, Area** – Location-based attributes.
- **Catdesc, Catcode** – : Category Description (Type of Connection) & Category Code (Code for connection Type)
- **Totservices** – Total number of EV charging services.
- **Billdservices** – Number of billed charging services.
- **Units** – Electricity consumption (kWh).
- **Load** – Load capacity (kW).

## 🚀 Analysis
- 📊 **Monthly Electricity Consumption Trends**
  ![EV_Data](https://github.com/rakesh-meka/TG-NPDCL_EV_charging_stations__Analysis/blob/main/Images/Monthly%20Electricity%20Consumption%20Trend%20(Jan%202024%20-%20Dec%202024).png)
  
- 🔝 **Top 10 Circles with Highest EV Consumption**
  ![EV_Data](https://github.com/rakesh-meka/TG-NPDCL_EV_charging_stations__Analysis/blob/main/Images/Top%2010%20Circles%20by%20Electricity%20Consumption%20in%20TG%20(Jan%202024%20-%20Dec%202024).png)
  
- 🔻 **Bottom 3 Circles with Lowest EV Consumption**
  ![EV_Data](https://github.com/rakesh-meka/TG-NPDCL_EV_charging_stations__Analysis/blob/main/Images/Bottom%203%20Circles%20in%20EV%20Charging%20Consumption%20(Jan-Dec%202024).png)
  
- 📉 **Billed vs. Unbilled Services Analysis**
  ![EV_Data](https://github.com/rakesh-meka/TG-NPDCL_EV_charging_stations__Analysis/blob/main/Images/Billed%20vs.%20Unbilled%20Services%20Over%20Time%20(Jan%202024%20-%20Dec%202024).png)
  
- 📈 **Seasonal Consumption Trends**

  ![EV_Data](https://github.com/rakesh-meka/TG-NPDCL_EV_charging_stations__Analysis/blob/main/Images/Electricity%20Consumption%20by%20Season.png)

- **Load vs. Electricity Consumption**

   ![EV_Data](https://github.com/rakesh-meka/TG-NPDCL_EV_charging_stations__Analysis/blob/main/Images/Load%20vs.%20Electricity%20Consumption%20(Jan%202024%20-%20Dec%202024).png)
  
## 🛠️ Technologies Used
- **Python** (Pandas, Matplotlib, Seaborn)
- **Jupyter Notebook**
- **CSV Data Processing**
- **GitHub for Version Control**

## 📄 Project Structure
```
📁 TG-NPDCL-EV-Analysis/
├── 📄 Project_NPDCL.ipynb  # Jupyter Notebook with analysis
├── 📂 Rawdata/ & Cleaned_data/  # Raw and cleaned datasets
├── 📄 final_sorted_output.csv  # Merged and cleaned dataset
├── 📄 README.md            # Project documentation
└── 📂 images/              # Graphs and visualizations
```

## 🔍 Insights & Recommendations
✅ Expand EV infrastructure in **low-consumption Circles**.  
✅ Plan electricity distribution based on **peak demand trends**.  
✅ Address billing inefficiencies by reducing **unbilled services**.  
✅ Promote **EV adoption in low-demand areas** through incentives.  

## 🤝 Contributing
Contributions are welcome! If you'd like to enhance this project:
1. **Fork the repository**
2. **Create a new branch** (`feature-branch`)
3. **Make your changes & commit**
4. **Submit a pull request**

## 📜 License
This project is licensed under the **MIT License**.

## 📬 Contact
For any queries, reach out via rakeshmeka.work@gmail.com.

---
🚗💡 **Driving towards a greener future with data-driven insights!**

