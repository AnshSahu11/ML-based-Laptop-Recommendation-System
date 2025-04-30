import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("laptops.csv")

# Encode categorical data
encoder = LabelEncoder()
for col in ["brand_name", "processor_brand", "gpu_brand", "os"]:
    df[col] = encoder.fit_transform(df[col])

# Normalize numerical features
scaler = MinMaxScaler()
df[["price", "ram_num", "memory_size", "core_num", "rating"]] = scaler.fit_transform(
    df[["price", "ram_num", "memory_size", "core_num", "rating"]])

# Compute similarity
features = ["brand_name", "processor_brand", "gpu_brand", "ram_num", "memory_size", "core_num", "rating", "price"]
similarity_matrix = cosine_similarity(df[features])

# Streamlit App
st.title("💻 AI-Powered Laptop Recommendation System")

# Add a search bar
search_query = st.text_input("🔍 Search for a Laptop Model", "")

# Filter laptops based on search query
filtered_laptops = df[df["model"].str.contains(search_query, case=False, na=False)]

# Select a laptop from filtered results
selected_laptop = st.selectbox("Select a Laptop", filtered_laptops["model"].values if not filtered_laptops.empty else ["No laptops found"])

# Only proceed if a valid laptop is selected
if selected_laptop != "No laptops found":
    # Get laptop index
    idx = df[df["model"] == selected_laptop].index[0]

    # Find most similar laptops
    similar_indices = similarity_matrix[idx].argsort()[-6:-1][::-1]
    similar_laptops = df.iloc[similar_indices][["model"]]

    # Show Recommendations
    st.subheader("📌 Recommended Laptops")
    st.dataframe(similar_laptops, use_container_width=True)

else:
    st.warning("No matching laptops found. Try a different search!")
