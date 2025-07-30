import plotly.graph_objs as go
import pandas as pd

def generate_interactive_plot(ImbalancePriceDKK, SpotPriceDKK, BalancingDemand, title):
    # Combine and align all Series
    data = pd.DataFrame({
        "Imbalance": ImbalancePriceDKK,
        "Spot": SpotPriceDKK,
        "Balancing Demand": BalancingDemand
    }).dropna()

    traces = []

    # --- Spot Price (black line) ---
    traces.append(go.Scatter(
        x=data.index,
        y=data["Spot"],
        mode="lines",
        name="Spot Price [EUR]",
        line=dict(color="black"),
        yaxis="y1"
    ))

    # --- Imbalance Price (color-changing line) ---
    condition = data["Imbalance"] > data["Spot"]
    prev_state = condition.iloc[0]
    segment_start = 0

    for i in range(1, len(data)):
        current_state = condition.iloc[i]
        if current_state != prev_state:
            segment = data.iloc[segment_start:i+1]
            traces.append(go.Scatter(
                x=segment.index,
                y=segment["Imbalance"],
                mode="lines",
                name="Imbalance Price [EUR]",
                line=dict(color="red" if prev_state else "blue"),
                showlegend=False,
                yaxis="y1"
            ))
            segment_start = i
            prev_state = current_state

    # Add final Imbalance segment
    segment = data.iloc[segment_start:]
    traces.append(go.Scatter(
        x=segment.index,
        y=segment["Imbalance"],
        mode="lines",
        name="Imbalance Price [EUR]",
        line=dict(color="red" if prev_state else "blue"),
        showlegend=True,
        yaxis="y1"
    ))

    # --- Balancing Demand (dashed green line on secondary axis) ---
    traces.append(go.Scatter(
        x=data.index,
        y=data["Balancing Demand"],
        mode="lines",
        name="Balancing Demand [MW]",
        line=dict(color="green"),
        yaxis="y2"
    ))

    layout = go.Layout(
        title=title,
        xaxis=dict(
            title="Date",
            tickformat="%H:%M\n%Y-%m-%d",
            dtick="D1",
            tickangle=45,
            tickfont=dict(size=10)
        ),
        yaxis=dict(
            title="Price [EUR]",
            side="left"
        ),
        yaxis2=dict(
            title="Balancing Demand [MW]",
            overlaying="y",
            side="right"
        ),
        legend=dict(x=0, y=1),
        margin=dict(l=50, r=50, t=50, b=50),
    )

    fig = go.Figure(data=traces, layout=layout)
    return fig
