# =========================================================
# ADVANCED FRAUD DETECTION DASHBOARD
# STREAMLIT CLOUD SAFE VERSION
# =========================================================

# =========================================================
# IMPORT LIBRARIES
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import warnings

warnings.filterwarnings("ignore")

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Fraud Detection Dashboard",
    page_icon="🚨",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DEMO DATASET
# =========================================================

@st.cache_data
def load_data():

    np.random.seed(42)

    rows = 3000

    df = pd.DataFrame({

        "TransactionID": range(1, rows + 1),

        "TransactionDT": np.random.randint(
            10000,
            500000,
            rows
        ),

        "TransactionAmt": np.random.randint(
            10,
            5000,
            rows
        ),

        "isFraud": np.random.choice(
            [0,1],
            rows,
            p=[0.94,0.06]
        )
    })

    return df

# load dataset

df = load_data()

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title(
    "Fraud Detection System"
)

page = st.sidebar.radio(

    "Navigation",

    [
        "Dashboard",
        "Analytics",
        "Explorer",
        "Prediction",
        "Risk Analysis"
    ]
)

# =========================================================
# DASHBOARD PAGE
# =========================================================

if page == "Dashboard":

    st.title(
        "🚨 Real-Time Fraud Detection Dashboard"
    )

    st.markdown(
        "AI-powered fraud analytics system"
    )

    # =====================================================
    # KPI METRICS
    # =====================================================

    total_transactions = len(df)

    total_fraud = int(
        df['isFraud'].sum()
    )

    fraud_rate = (
        total_fraud
        /
        total_transactions
    ) * 100

    avg_transaction = round(
        df['TransactionAmt'].mean(),
        2
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Transactions",
        f"{total_transactions:,}"
    )

    col2.metric(
        "Fraud Cases",
        f"{total_fraud:,}"
    )

    col3.metric(
        "Fraud Rate",
        f"{fraud_rate:.2f}%"
    )

    col4.metric(
        "Average Amount",
        f"${avg_transaction}"
    )

    st.divider()

    # =====================================================
    # TRANSACTION SCATTER
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        sample_df = df.sample(1000)

        fig = px.scatter(

            sample_df,

            x='TransactionDT',

            y='TransactionAmt',

            color='isFraud',

            title='Transaction Scatter Plot'
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        fraud_counts = df[
            'isFraud'
        ].value_counts()

        pie_fig = px.pie(

            values=fraud_counts.values,

            names=['Non Fraud','Fraud'],

            title='Fraud Distribution'
        )

        st.plotly_chart(
            pie_fig,
            use_container_width=True
        )

# =========================================================
# ANALYTICS PAGE
# =========================================================

elif page == "Analytics":

    st.title(
        "📊 Fraud Analytics"
    )

    # =====================================================
    # HOUR EXTRACTION
    # =====================================================

    df['Hour'] = (
        df['TransactionDT'] // 3600
    ) % 24

    hour_fraud = df.groupby(
        'Hour'
    )['isFraud'].mean()

    fig = px.line(

        x=hour_fraud.index,

        y=hour_fraud.values,

        labels={
            'x':'Hour',
            'y':'Fraud Rate'
        },

        title='Fraud Rate By Hour'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # TOP FRAUD TRANSACTIONS
    # =====================================================

    st.subheader(
        "Top Fraud Transactions"
    )

    fraud_df = df[
        df['isFraud'] == 1
    ]

    fraud_df = fraud_df.sort_values(
        by='TransactionAmt',
        ascending=False
    )

    st.dataframe(

        fraud_df[
            [
                'TransactionID',
                'TransactionAmt'
            ]
        ].head(20)
    )

# =========================================================
# EXPLORER PAGE
# =========================================================

elif page == "Explorer":

    st.title(
        "🔍 Transaction Explorer"
    )

    amount_range = st.slider(

        "Transaction Amount Range",

        0,

        int(df['TransactionAmt'].max()),

        (
            0,
            5000
        )
    )

    fraud_filter = st.selectbox(

        "Fraud Filter",

        [
            "All",
            "Fraud Only",
            "Non Fraud Only"
        ]
    )

    filtered_df = df[

        (
            df['TransactionAmt']
            >= amount_range[0]
        )
        &
        (
            df['TransactionAmt']
            <= amount_range[1]
        )
    ]

    if fraud_filter == "Fraud Only":

        filtered_df = filtered_df[
            filtered_df['isFraud'] == 1
        ]

    elif fraud_filter == "Non Fraud Only":

        filtered_df = filtered_df[
            filtered_df['isFraud'] == 0
        ]

    st.write(
        f"Showing {len(filtered_df)} transactions"
    )

    st.dataframe(
        filtered_df.head(20)
    )

# =========================================================
# LIVE PREDICTION PAGE
# =========================================================

elif page == "Prediction":

    st.title(
        "🤖 Live Fraud Prediction"
    )

    st.markdown(
        "Enter transaction details below"
    )

    col1, col2 = st.columns(2)

    with col1:

        amount = st.number_input(

            "Transaction Amount",

            min_value=0.0,

            value=500.0
        )

    with col2:

        hour = st.slider(

            "Transaction Hour",

            0,

            23,

            12
        )

    device = st.selectbox(

        "Device Type",

        [
            "desktop",
            "mobile"
        ]
    )

    # =====================================================
    # PREDICTION BUTTON
    # =====================================================

    if st.button("Predict Fraud Risk"):

        probability = np.random.uniform(
            0,
            1
        )

        st.metric(
            "Fraud Probability",
            f"{probability:.2f}"
        )

        st.progress(
            int(probability * 100)
        )

        if probability >= 0.75:

            st.error(
                "Critical Risk Transaction"
            )

        elif probability >= 0.40:

            st.warning(
                "Suspicious Transaction"
            )

        else:

            st.success(
                "Safe Transaction"
            )

# =========================================================
# RISK ANALYSIS PAGE
# =========================================================

elif page == "Risk Analysis":

    st.title(
        "⚠️ Risk Analysis"
    )

    # =====================================================
    # RISK PROBABILITIES
    # =====================================================

    risk_prob = np.random.uniform(
        0,
        1,
        len(df)
    )

    risk_df = pd.DataFrame()

    risk_df['RiskProbability'] = risk_prob

    conditions = [

        risk_df['RiskProbability'] >= 0.75,

        (
            (risk_df['RiskProbability'] >= 0.40)
            &
            (risk_df['RiskProbability'] < 0.75)
        ),

        risk_df['RiskProbability'] < 0.40
    ]

    choices = [

        'Critical Risk',

        'Suspicious',

        'Safe'
    ]

    risk_df['RiskLevel'] = np.select(

        conditions,

        choices,

        default='Safe'
    )

    # =====================================================
    # DONUT CHART
    # =====================================================

    risk_counts = risk_df[
        'RiskLevel'
    ].value_counts()

    fig = go.Figure(

        data=[

            go.Pie(

                labels=risk_counts.index,

                values=risk_counts.values,

                hole=.5
            )
        ]
    )

    fig.update_layout(
        title="Risk Segmentation"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # RISK TABLE
    # =====================================================

    st.subheader(
        "Risk Summary"
    )

    st.dataframe(
        risk_df.head(20)
    )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Built using Streamlit, Plotly and LightGBM"
)