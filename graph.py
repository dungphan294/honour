import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def load_data(file_path):
    """Load and return the CSV data"""
    return pd.read_csv(file_path)

def calculate_project_influences(sample_df, max_capacity, max_investment):
    """Calculate influence scores between all projects in the sample"""
    influence_scores = []
    for i, row1 in sample_df.iterrows():
        for j, row2 in sample_df.iterrows():
            if i != j:
                # Technology similarity (T_ij)
                T = 1 if row1['Technology'] == row2['Technology'] else 0
                
                # Geography similarity (G_ij)
                G = 1 if row1['Country'] == row2['Country'] else 0
                
                # Capacity similarity (C_ij)
                C = 1 - abs(row1['Capacity (kt H2/y)'] - row2['Capacity (kt H2/y)']) / max_capacity
                
                # Calculate influence score
                S = 0.5 * T + 0.3 * G + 0.2 * C
                
                influence_scores.append({
                    'Project1': row1['Project Name'],
                    'Project2': row2['Project Name'],
                    'Score': S,
                    'Technology1': row1['Technology'],
                    'Country1': row1['Country'],
                    'Capacity1': row1['Capacity (kt H2/y)'],
                    'Investment1': row1['Investment Cost (MUSD)'],
                    'Date1': row1['Date Online'],
                    'Technology2': row2['Technology'],
                    'Country2': row2['Country'],
                    'Capacity2': row2['Capacity (kt H2/y)'],
                    'Investment2': row2['Investment Cost (MUSD)'],
                    'Date2': row2['Date Online']
                })
    return pd.DataFrame(influence_scores)

def create_3d_scatter_plot(scores_df, color_scale='Viridis', marker_size=5, opacity=0.7, title='Project Influence Scores'):
    """Create 3D scatter plot of influence scores
    
    Args:
        scores_df (pd.DataFrame): DataFrame containing project scores and data
        color_scale (str, optional): Plotly colorscale name. Defaults to 'Viridis'.
        marker_size (int, optional): Size of scatter points. Defaults to 5.
        opacity (float, optional): Opacity of scatter points (0-1). Defaults to 0.7.
        title (str, optional): Plot title. Defaults to 'Project Influence Scores'.
    
    Returns:
        plotly.graph_objects.Figure: Interactive 3D scatter plot
    """
    # Create the scatter plot
    fig = px.scatter_3d(scores_df,
                        x='Capacity1',
                        y='Investment1',
                        z='Score',
                        color='Score',
                        hover_data=['Project1', 'Project2', 'Technology1', 'Technology2', 'Country1', 'Country2', 'Date1', 'Date2', 'Capacity2', 'Investment2'],
                        title=title,
                        color_continuous_scale=color_scale,
                        labels={
                            'Capacity': 'Capacity (kt H2/y)',
                            'Investment': 'Investment Cost (MUSD)',
                            'Score': 'Influence Score'
                        })

    # Enhanced hover template with more project details
    fig.update_traces(
        marker=dict(size=marker_size),
        opacity=opacity,
        hovertemplate="<br>".join([
            "<b>Project 1:</b> %{customdata[0]}",
            "Technology: %{customdata[2]}",
            "Country: %{customdata[4]}",
            "Capacity: %{x:.1f} kt H2/y",
            "Investment: %{y:.1f} MUSD",
            "Influence Score: %{z:.3f}",
            "Date Online: %{customdata[6]}",
            "<br>",
            "<b>Project 2:</b> %{customdata[1]}",
            "Technology: %{customdata[3]}",
            "Country: %{customdata[5]}",
            "Capacity: %{customdata[8]:.1f} kt H2/y",
            "Investment: %{customdata[9]:.1f} MUSD",
            "Date Online: %{customdata[7]}",
            "<br>",
            "<b>Influence Score:</b> %{z:.3f}"
        ])
    )

    # Enhanced layout configuration
    fig.update_layout(
        scene=dict(
            camera=dict(
                up=dict(x=0, y=0, z=1),
                center=dict(x=0, y=0, z=0),
                eye=dict(x=1.5, y=1.5, z=1.5)
            ),
            xaxis=dict(
                title='Capacity (kt H2/y)',
                showgrid=True,
                gridwidth=1,
                gridcolor='lightgray'
            ),
            yaxis=dict(
                title='Investment Cost (MUSD)',
                showgrid=True,
                gridwidth=1,
                gridcolor='lightgray'
            ),
            zaxis=dict(
                title='Influence Score',
                showgrid=True,
                gridwidth=1,
                gridcolor='lightgray'
            ),
            bgcolor='white'
        ),
        title=dict(
            text=title,
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor='top'
        ),
        margin=dict(l=0, r=0, t=30, b=0),
        showlegend=False
    )

    return fig

def create_country_heatmap(scores_df):
    """Create heatmap of average influence scores by country"""
    country_scores = scores_df.groupby(['Country1', 'Country2'])['Score'].mean().reset_index()
    country_pivot = country_scores.pivot(index='Country1', columns='Country2', values='Score')
    
    fig = px.imshow(country_pivot,
                    title='Average Influence Scores Between Countries',
                    labels=dict(x='Country 2', y='Country 1', color='Influence Score'))
    return fig

def save_plots(fig1, fig2, file1='influence_scores_3d.html', file2='country_influence_heatmap.html'):
    """Save plots to HTML files"""
    fig1.write_html(file1, auto_open=True)
    fig2.write_html(file2, auto_open=True)

def save_scores_to_csv(scores_df, filename='project_influence_scores.csv'):
    """Save the influence scores DataFrame to a CSV file
    
    Args:
        scores_df (pd.DataFrame): DataFrame containing project scores and data
        filename (str, optional): Name of output CSV file. Defaults to 'project_influence_scores.csv'
    """
    scores_df.to_csv(filename, index=False)
    print(f"Scores saved to {filename}")

def main():
    # Load data
    df = load_data('europe_data.csv')
    
    # Sample projects
    sample_size = 20
    sample_df = df.sample(n=sample_size, random_state=42)
    
    # Calculate maximum values for normalization
    max_capacity = df['Capacity (kt H2/y)'].max()
    max_investment = df['Investment Cost (MUSD)'].max()
    
    # Calculate influence scores
    scores_df = calculate_project_influences(sample_df, max_capacity, max_investment)
    
    # Save scores to CSV
    save_scores_to_csv(scores_df)
    
    # Create visualizations
    scatter_plot = create_3d_scatter_plot(scores_df)
    heatmap = create_country_heatmap(scores_df)
    
    # Save plots
    save_plots(scatter_plot, heatmap)

if __name__ == "__main__":
    main()