from flask import Flask, request, jsonify, render_template, url_for
from datetime import datetime, timedelta
from get_data import fetch_energinet_now_data
from src.plots import generate_interactive_plot
import os
import time

app = Flask(__name__)

# Helper to save plot and return a cache-busted URL
def save_plot(fig, filename):
    filepath = os.path.join('static', filename)
    fig.write_html(filepath, auto_open=False)
    timestamp = int(time.time())
    return url_for('static', filename=filename) + f'?v={timestamp}'

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        df = fetch_energinet_now_data(2880)
        df.set_index("TimeDK", inplace=True)

        now = datetime.now()
        end_time = now - timedelta(hours=1)
        time_now = now.strftime("%H:%M:%S")
        start_time = end_time - timedelta(days=14) - timedelta(hours=int(time_now.split(":")[0]))

        filtered_df = df.loc[(df.index >= start_time) & (df.index <= end_time)]

        # -------------------- DK1 --------------------
        filtered_dk1 = filtered_df[filtered_df['PriceArea'] == 'DK1']

        plot_url = save_plot(generate_interactive_plot(
            ImbalancePriceDKK=filtered_dk1['ImbalancePriceEUR'],
            SpotPriceDKK=filtered_dk1['SpotPriceEUR'],
            BalancingDemand=filtered_dk1['BalancingDemand'],
            title="Electricity Prices and Imbalance Prices DK1"
        ), filename='plot.html')

        plot_urls_dk1 = []
        for i, minute in enumerate([0, 15, 30, 45]):
            filtered = filtered_dk1[filtered_dk1.index.minute == minute]
            fig = generate_interactive_plot(
                ImbalancePriceDKK=filtered['ImbalancePriceEUR'],
                SpotPriceDKK=filtered['SpotPriceEUR'],
                BalancingDemand=filtered['BalancingDemand'],
                title=f"Electricity Prices and Imbalance Prices DK1 quarter {i+1}"
            )
            plot_urls_dk1.append(save_plot(fig, filename=f'plot{i+3}.html'))  # plot3.html - plot6.html

        # -------------------- DK2 --------------------
        filtered_dk2 = filtered_df[filtered_df['PriceArea'] == 'DK2']

        plot_url2 = save_plot(generate_interactive_plot(
            ImbalancePriceDKK=filtered_dk2['ImbalancePriceEUR'],
            SpotPriceDKK=filtered_dk2['SpotPriceEUR'],
            BalancingDemand=filtered_dk2['BalancingDemand'],
            title="Electricity Prices and Imbalance Prices DK2"
        ), filename='plot2.html')

        plot_urls_dk2 = []
        for i, minute in enumerate([0, 15, 30, 45]):
            filtered = filtered_dk2[filtered_dk2.index.minute == minute]
            fig = generate_interactive_plot(
                ImbalancePriceDKK=filtered['ImbalancePriceEUR'],
                SpotPriceDKK=filtered['SpotPriceEUR'],
                BalancingDemand=filtered['BalancingDemand'],
                title=f"Electricity Prices and Imbalance Prices DK2 quarter {i+1}"
            )
            plot_urls_dk2.append(save_plot(fig, filename=f'plot2_{i}.html'))

        return render_template(
            'view_data.html',
            plot=plot_url,
            plot2=plot_url2,
            plot3=plot_urls_dk1[0],
            plot4=plot_urls_dk1[1],
            plot5=plot_urls_dk1[2],
            plot6=plot_urls_dk1[3],
            plot2_0=plot_urls_dk2[0],
            plot2_1=plot_urls_dk2[1],
            plot2_2=plot_urls_dk2[2],
            plot2_3=plot_urls_dk2[3]
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
