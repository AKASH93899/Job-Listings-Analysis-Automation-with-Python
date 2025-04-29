import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime

print("\n📊 Auto Job Listings Report Started...\n")

while True:
    print(f"🔄 Updating report at {datetime.now().strftime('%Y-%m-%d %H:%M')}...")

    # ───── STEP 1: LOAD DATA ─────
    df = pd.read_csv("c://Users//Akash Sharma//OneDrive//Desktop//job_listings_2023_2024.csv", parse_dates=["Posted Date"])
    df.dropna(inplace=True)

    # ───── STEP 2: PREPARE DATA ─────
    df["Year"] = df["Posted Date"].dt.year
    total_jobs = len(df)
    avg_salary = df["Salary (INR LPA)"].mean()
    top_location = df["Location"].value_counts().idxmax()
    top_skills = df["Skills"].str.split(', ').explode().value_counts().head(5)

    # ───── STEP 3: CREATE CHARTS ─────
    # 1. Jobs by Year
    df["Year"].value_counts().sort_index().plot(kind="bar", color="skyblue", title="Jobs by Year")
    plt.ylabel("No. of Jobs")
    plt.tight_layout()
    plt.savefig("jobs_by_year.png")
    plt.show()  # Display the chart
    plt.close()

    # 2. Top Locations
    df["Location"].value_counts().head(5).plot(kind="barh", color="lightgreen", title="Top Job Locations")
    plt.xlabel("Job Count")
    plt.tight_layout()
    plt.savefig("top_locations.png")
    plt.show()  # Display the chart
    plt.close()

    # 3. Top Skills
    top_skills.plot(kind="bar", color="salmon", title="Top Skills Required")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("top_skills.png")
    plt.show()  # Display the chart
    plt.close()

    # ───── STEP 4: SAVE TEXT REPORT ─────
    # Save the report inside the loop to ensure it updates
    with open("job_report.txt", "w", encoding="utf-8") as file:
        file.write("📄 Job Listings Analysis Report\n")
        file.write(f"📅 Updated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        file.write(f"🧾 Total Jobs: {total_jobs}\n")
        file.write(f"💰 Average Salary: ₹{avg_salary:.2f} LPA\n")
        file.write(f"📍 Top Hiring Location: {top_location}\n")
        file.write("\n📊 Charts Saved:\n")
        file.write(" - jobs_by_year.png\n")
        file.write(" - top_locations.png\n")
        file.write(" - top_skills.png\n")

    print("✅ Report and Charts Updated Successfully!\n")

    # ───── STEP 5: WAIT 1 MINUTE ─────
    time.sleep(60)
