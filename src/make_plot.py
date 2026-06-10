import plotly.graph_objects as go


def plot_power_curve(power_curve):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=power_curve["zeit_sek"],
        y=power_curve["leistung_w"],
        mode='lines',
        line=dict(color='crimson', width=2),
        hovertemplate='Zeit: %{x}s<br>Leistung: %{y:.0f} W<extra></extra>'
    ))


    tickvals = [1, 5, 10, 30, 60, 120, 300, 600, 900, 1200, 1800]
    ticktext = ['1s', '5s', '10s', '30s', '1:00', '2:00', '5:00', '10:00', '15:00', '20:00', '30:00']

    fig.update_layout(
        title='Power Curve',
        xaxis=dict(
        title='Zeit (mm:ss)',
        type='log',
        tickvals=tickvals,
        ticktext=ticktext
    ),
    yaxis_title='Beste Leistung (Watt)',
    hovermode='x'
    )

    fig.show()
    fig.write_image("screenshot.png")
