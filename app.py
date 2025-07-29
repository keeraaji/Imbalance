from flask import Flask, request, jsonify, render_template, url_for, redirect
from datetime import datetime, timedelta
from get_data import fetch_energinet_now_data
from src.plots import generate_interactive_plot
import os

app = Flask(__name__, static_folder='static')




@app.route('/', methods=['GET', 'POST'])
def home():
    try:
       
        
        df = fetch_energinet_now_data(2880)

        #Time series index

        df.set_index("TimeDK", inplace=True)


        # Current time (local DK time assumed if TimeDK is local)
        now = datetime.now()

        # Find time now
        time_now = now.strftime("%H:%M:%S")

        # Calculate time range: from 14 days ago to 1 hour before now
        end_time = now - timedelta(hours=1)
        start_time = end_time - timedelta(days=14) - timedelta(hours=int(time_now.split(":")[0]))

        # Filter the DataFrame (assumes TimeDK is datetime index)
        filtered_df = df.loc[(df.index >= start_time) & (df.index <= end_time)]


        # Filter by PriceArea
        filtered_dk1 = filtered_df[filtered_df['PriceArea'] == 'DK1']

        spotprice_filtered_dk1 = filtered_dk1['SpotPriceEUR']
        imbalance_price_filtered_dk1 = filtered_dk1['ImbalancePriceEUR']
        balancingDemand_filtered_dk1 = filtered_dk1['BalancingDemand']
        fig = generate_interactive_plot(
            ImbalancePriceDKK=imbalance_price_filtered_dk1,
            SpotPriceDKK=spotprice_filtered_dk1, BalancingDemand=balancingDemand_filtered_dk1, title="Electricity Prices and Imbalance Prices DK1"
        )
        plot_file_path = os.path.join('static', 'plot.html')
        fig.write_html(plot_file_path, auto_open=False)
        plot_url = url_for('static', filename='plot.html')

       

        filtered_dk1_0 = filtered_dk1[filtered_dk1.index.minute == 0]

        spotprice_filtered_dk1_0 = filtered_dk1_0['SpotPriceEUR']
        imbalance_price_filtered_dk1_0 = filtered_dk1_0['ImbalancePriceEUR']
        balancingDemand_filtered_dk1_0 = filtered_dk1_0['BalancingDemand']
        # Generate plots for each quarter of the hour
        # First quarter (0-15 minutes)
        fig3 = generate_interactive_plot(
            ImbalancePriceDKK=imbalance_price_filtered_dk1_0,
            SpotPriceDKK=spotprice_filtered_dk1_0, BalancingDemand=balancingDemand_filtered_dk1_0, title="Electricity Prices and Imbalance Prices DK1 first quarters"
        )
        plot_file_path3 = os.path.join('static', 'plot3.html')
        fig3.write_html(plot_file_path3, auto_open=False)
        plot_url3 = url_for('static', filename='plot3.html')

        filtered_dk1_1 = filtered_dk1[filtered_dk1.index.minute == 15]

        spotprice_filtered_dk1_1 = filtered_dk1_1['SpotPriceEUR']
        imbalance_price_filtered_dk1_1 = filtered_dk1_1['ImbalancePriceEUR']
        balancingDemand_filtered_dk1_1 = filtered_dk1_1['BalancingDemand']
        fig4 = generate_interactive_plot(
            ImbalancePriceDKK=imbalance_price_filtered_dk1_1,
            SpotPriceDKK=spotprice_filtered_dk1_1, BalancingDemand=balancingDemand_filtered_dk1_1, title="Electricity Prices and Imbalance Prices DK1 second quarters"
        )
        plot_file_path4 = os.path.join('static', 'plot4.html')
        fig4.write_html(plot_file_path4, auto_open=False)
        plot_url4 = url_for('static', filename='plot4.html')
        filtered_dk1_2 = filtered_dk1[filtered_dk1.index.minute == 30]
        spotprice_filtered_dk1_2 = filtered_dk1_2['SpotPriceEUR']
        imbalance_price_filtered_dk1_2 = filtered_dk1_2['ImbalancePriceEUR']
        balancingDemand_filtered_dk1_2 = filtered_dk1_2['BalancingDemand']
        # Third quarter (30-45 minutes)
        fig5 = generate_interactive_plot(
            ImbalancePriceDKK=imbalance_price_filtered_dk1_2,
            SpotPriceDKK=spotprice_filtered_dk1_2, BalancingDemand=balancingDemand_filtered_dk1_2, title="Electricity Prices and Imbalance Prices DK1 third quarters"
        )
        plot_file_path5 = os.path.join('static', 'plot5.html')
        fig5.write_html(plot_file_path5, auto_open=False)
        plot_url5 = url_for('static', filename='plot5.html')
        filtered_dk1_3 = filtered_dk1[filtered_dk1.index.minute == 45]
        spotprice_filtered_dk1_3 = filtered_dk1_3['SpotPriceEUR']
        imbalance_price_filtered_dk1_3 = filtered_dk1_3['ImbalancePriceEUR']
        balancingDemand_filtered_dk1_3 = filtered_dk1_3['BalancingDemand']
        # Fourth quarter (45-59 minutes)
        fig6 = generate_interactive_plot(
            ImbalancePriceDKK=imbalance_price_filtered_dk1_3,
            SpotPriceDKK=spotprice_filtered_dk1_3, BalancingDemand=balancingDemand_filtered_dk1_3, title="Electricity Prices and Imbalance Prices DK1 fourth quarters"
        )
        plot_file_path6 = os.path.join('static', 'plot6.html')
        fig6.write_html(plot_file_path6, auto_open=False)
        plot_url6 = url_for('static', filename='plot6.html')

         # Filter by PriceArea
        filtered_dk2 = filtered_df[filtered_df['PriceArea'] == 'DK2']

        spotprice_filtered_dk2 = filtered_dk2['SpotPriceEUR']
        imbalance_price_filtered_dk2 = filtered_dk2['ImbalancePriceEUR']
        balancingDemand_filtered_dk2 = filtered_dk2['BalancingDemand']
        fig = generate_interactive_plot(
            ImbalancePriceDKK=imbalance_price_filtered_dk2,
            SpotPriceDKK=spotprice_filtered_dk2, BalancingDemand=balancingDemand_filtered_dk2, title="Electricity Prices and Imbalance Prices DK2"
        )
        plot_file_path2 = os.path.join('static', 'plot2.html')
        fig.write_html(plot_file_path2, auto_open=False)
        plot_url2 = url_for('static', filename='plot2.html')

        filtered_dk2_0 = filtered_dk2[filtered_dk2.index.minute == 0]
        spotprice_filtered_dk2_0 = filtered_dk2_0['SpotPriceEUR']
        imbalance_price_filtered_dk2_0 = filtered_dk2_0['ImbalancePriceEUR']
        balancingDemand_filtered_dk2_0 = filtered_dk2_0['BalancingDemand']
        fig7 = generate_interactive_plot(
            ImbalancePriceDKK=imbalance_price_filtered_dk2_0,
            SpotPriceDKK=spotprice_filtered_dk2_0, BalancingDemand=balancingDemand_filtered_dk2_0, title="Electricity Prices and Imbalance Prices DK2 first quarters"
        )
        plot_file_path2_0 = os.path.join('static', 'plot2_0.html')
        fig7.write_html(plot_file_path2_0, auto_open=False)
        plot_url2_0 = url_for('static', filename='plot2_0.html')
        filtered_dk2_1 = filtered_dk2[filtered_dk2.index.minute == 15]
        spotprice_filtered_dk2_1 = filtered_dk2_1['SpotPriceEUR']
        imbalance_price_filtered_dk2_1 = filtered_dk2_1['ImbalancePriceEUR']
        balancingDemand_filtered_dk2_1 = filtered_dk2_1['BalancingDemand']
        fig8 = generate_interactive_plot(           
            ImbalancePriceDKK=imbalance_price_filtered_dk2_1,
            SpotPriceDKK=spotprice_filtered_dk2_1, BalancingDemand=balancingDemand_filtered_dk2_1, title="Electricity Prices and Imbalance Prices DK2 second quarters"
        )
        plot_file_path2_1 = os.path.join('static', 'plot2_1.html')
        fig8.write_html(plot_file_path2_1, auto_open=False)
        plot_url2_1 = url_for('static', filename='plot2_1.html')
        filtered_dk2_2 = filtered_dk2[filtered_dk2.index.minute == 30]
        spotprice_filtered_dk2_2 = filtered_dk2_2['SpotPriceEUR']
        imbalance_price_filtered_dk2_2 = filtered_dk2_2['ImbalancePriceEUR']
        balancingDemand_filtered_dk2_2 = filtered_dk2_2['BalancingDemand']
        fig9 = generate_interactive_plot(
            ImbalancePriceDKK=imbalance_price_filtered_dk2_2,
            SpotPriceDKK=spotprice_filtered_dk2_2, BalancingDemand=balancingDemand_filtered_dk2_2, title="Electricity Prices and Imbalance Prices DK2 third quarters"
        )
        plot_file_path2_2 = os.path.join('static', 'plot2_2.html')
        fig9.write_html(plot_file_path2_2, auto_open=False)
        plot_url2_2 = url_for('static', filename='plot2_2.html')
        filtered_dk2_3 = filtered_dk2[filtered_dk2.index.minute == 45]
        spotprice_filtered_dk2_3 = filtered_dk2_3['SpotPriceEUR']
        imbalance_price_filtered_dk2_3 = filtered_dk2_3['ImbalancePriceEUR']
        balancingDemand_filtered_dk2_3 = filtered_dk2_3['BalancingDemand']
        fig10 = generate_interactive_plot(
            ImbalancePriceDKK=imbalance_price_filtered_dk2_3,
            SpotPriceDKK=spotprice_filtered_dk2_3, BalancingDemand=balancingDemand_filtered_dk2_3, title="Electricity Prices and Imbalance Prices DK2 fourth quarters"
        )
        plot_file_path2_3 = os.path.join('static', 'plot2_3.html')
        fig10.write_html(plot_file_path2_3, auto_open=False)
        plot_url2_3 = url_for('static', filename='plot2_3.html')    

        return render_template('view_data.html', plot=plot_url, plot2=plot_url2, plot3=plot_url3, plot4=plot_url4, plot5=plot_url5, plot6=plot_url6,
                               plot2_0=plot_url2_0, plot2_1=plot_url2_1, plot2_2=plot_url2_2, plot2_3=plot_url2_3)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
