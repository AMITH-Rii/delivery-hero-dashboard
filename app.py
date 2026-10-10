import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Delivery Hero - AI Data Analyst",
    page_icon="🚚",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("data.csv")

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🚚 Delivery Hero – AI Data Analyst Dashboard")

st.write(
    "Improving Data Discoverability through AI-powered Data Analysis"
)

st.divider()

# --------------------------------------------------
# SIDEBAR - DATA DISCOVERY
# --------------------------------------------------

st.sidebar.title("🔎 Data Discovery")

categories = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=list(df["Category"].unique())
)

filtered_df = df[df["Category"].isin(categories)]

# --------------------------------------------------
# DASHBOARD OVERVIEW
# --------------------------------------------------

st.header("📊 Dashboard Overview")

if len(filtered_df) > 0:

    total_orders = filtered_df["Orders"].sum()
    total_revenue = filtered_df["Revenue"].sum()
    avg_delivery = filtered_df["Delivery_Time"].mean()
    avg_rating = filtered_df["Customer_Rating"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📦 Total Orders",
            f"{total_orders:,}"
        )

    with col2:
        st.metric(
            "💰 Total Revenue",
            f"₹{total_revenue:,}"
        )

    with col3:
        st.metric(
            "🚚 Avg Delivery Time",
            f"{avg_delivery:.1f} min"
        )

    with col4:
        st.metric(
            "⭐ Avg Rating",
            f"{avg_rating:.2f}"
        )

else:
    st.warning("Please select at least one category.")

st.divider()

# --------------------------------------------------
# DATA ANALYSIS CHARTS
# --------------------------------------------------

st.header("📈 Data Analysis")

if len(filtered_df) > 0:

    st.subheader("📦 Orders by Product")

    orders_chart = filtered_df[
        ["Product", "Orders"]
    ].set_index("Product")

    st.bar_chart(orders_chart)

    st.subheader("💰 Revenue by Product")

    revenue_chart = filtered_df[
        ["Product", "Revenue"]
    ].set_index("Product")

    st.bar_chart(revenue_chart)

    st.subheader("🚚 Delivery Time by Product")

    delivery_chart = filtered_df[
        ["Product", "Delivery_Time"]
    ].set_index("Product")

    st.bar_chart(delivery_chart)

st.divider()

# --------------------------------------------------
# PRODUCT PERFORMANCE
# --------------------------------------------------

st.header("📦 Product Performance")

if len(filtered_df) > 0:

    for index, row in filtered_df.iterrows():

        st.subheader(f"🛍️ {row['Product']}")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.write("**Category**")
            st.write(row["Category"])

        with col2:
            st.write("**Orders**")
            st.write(f"{row['Orders']:,}")

        with col3:
            st.write("**Revenue**")
            st.write(f"₹{row['Revenue']:,}")

        with col4:
            st.write("**Delivery Time**")
            st.write(f"{row['Delivery_Time']} min")

        st.progress(
            min(row["Customer_Rating"] / 5, 1.0),
            text=f"Customer Rating: {row['Customer_Rating']} / 5"
        )

        st.divider()

# --------------------------------------------------
# DATA DISCOVERY TABLE
# --------------------------------------------------

st.header("📋 Data Discovery Table")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# AI DATA INSIGHTS
# --------------------------------------------------

st.header("🤖 AI Data Insights")

if len(filtered_df) > 0:

    fastest = filtered_df.loc[
        filtered_df["Delivery_Time"].idxmin()
    ]

    highest_revenue = filtered_df.loc[
        filtered_df["Revenue"].idxmax()
    ]

    highest_orders = filtered_df.loc[
        filtered_df["Orders"].idxmax()
    ]

    highest_rating = filtered_df.loc[
        filtered_df["Customer_Rating"].idxmax()
    ]

    st.success(
        f"🚚 **Fastest Delivery:** {fastest['Product']} "
        f"({fastest['Delivery_Time']} minutes)"
    )

    st.info(
        f"💰 **Highest Revenue:** {highest_revenue['Product']} "
        f"(₹{highest_revenue['Revenue']:,})"
    )

    st.warning(
        f"📦 **Highest Orders:** {highest_orders['Product']} "
        f"({highest_orders['Orders']:,} orders)"
    )

    st.success(
        f"⭐ **Highest Rating:** {highest_rating['Product']} "
        f"({highest_rating['Customer_Rating']} / 5)"
    )

st.divider()

# --------------------------------------------------
# ASK AI DATA ANALYST
# --------------------------------------------------

st.header("💬 Ask AI Data Analyst")

query = st.text_input(
    "Ask a question about the data:",
    placeholder="Example: Which product has the highest revenue?"
)

if query and len(filtered_df) > 0:

    query_lower = query.lower()

    if "highest revenue" in query_lower:

        result = filtered_df.loc[
            filtered_df["Revenue"].idxmax()
        ]

        st.success(
            f"💰 **{result['Product']}** has the highest revenue "
            f"of **₹{result['Revenue']:,}**."
        )

    elif "highest orders" in query_lower:

        result = filtered_df.loc[
            filtered_df["Orders"].idxmax()
        ]

        st.success(
            f"📦 **{result['Product']}** has the highest number "
            f"of orders: **{result['Orders']:,}**."
        )

    elif "fastest" in query_lower:

        result = filtered_df.loc[
            filtered_df["Delivery_Time"].idxmin()
        ]

        st.success(
            f"🚚 **{result['Product']}** has the fastest delivery "
            f"time of **{result['Delivery_Time']} minutes**."
        )

    elif "highest rating" in query_lower:

        result = filtered_df.loc[
            filtered_df["Customer_Rating"].idxmax()
        ]

        st.success(
            f"⭐ **{result['Product']}** has the highest rating "
            f"of **{result['Customer_Rating']} / 5**."
        )

    elif "average delivery" in query_lower:

        average = filtered_df["Delivery_Time"].mean()

        st.info(
            f"🚚 Average delivery time is "
            f"**{average:.1f} minutes**."
        )

    elif "average rating" in query_lower:

        average = filtered_df["Customer_Rating"].mean()

        st.info(
            f"⭐ Average customer rating is "
            f"**{average:.2f} / 5**."
        )

    elif "total orders" in query_lower:

        total = filtered_df["Orders"].sum()

        st.info(
            f"📦 Total orders are **{total:,}**."
        )

    elif "total revenue" in query_lower:

        total = filtered_df["Revenue"].sum()

        st.info(
            f"💰 Total revenue is **₹{total:,}**."
        )

    else:

        st.info(
            "Try asking:\n\n"
            "• Which product has the highest revenue?\n"
            "• Which product has the highest orders?\n"
            "• Which product has the fastest delivery?\n"
            "• Which product has the highest rating?\n"
            "• What is the total revenue?\n"
            "• What is the average delivery time?"
        )

st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "Delivery Hero | AI Data Analyst | Data Discovery Dashboard"
)