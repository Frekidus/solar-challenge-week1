# BSWO Solar Data Discovery Dashboard Development

## Development Process
1. Created branch `dashboard-dev` to isolate dashboard development.
2. Designed folder structure with `app/` (containing `main.py` and `utils.py`) and `scripts/` (containing this README).
3. Developed `app/main.py` with Streamlit to include:
   - Country selection dropdown.
   - GHI boxplot visualization.
   - Top regions table filtered by a GHI threshold slider.
   - Reset button for interactivity.
4. Implemented `app/utils.py` with placeholder functions to simulate data processing and plotting.
5. Tested locally using `streamlit run app/main.py`.
6. Committed initial code with "feat: basic Streamlit UI" and additional commits for enhancements.

## Usage Instructions
1. Ensure Streamlit is installed: `pip install streamlit`.
2. Navigate to the `app/` directory.
3. Run the dashboard locally: `streamlit run main.py`.
4. Interact with the dashboard:
   - Select a country from the dropdown.
   - Adjust the GHI threshold using the slider.
   - Click "Reset GHI Threshold" to revert to the default.
5. Deploy to Streamlit Community Cloud:
   - Push `app/` and `scripts/` to a new GitHub repository.
   - Link to Streamlit Community Cloud for deployment.
   - Access the live URL (e.g., `https://solar-dashboard.streamlit.app` after deployment).

## Notes
- This is a code-only implementation; actual data should be integrated in a production environment.
- Deployment requires a public GitHub repository and Streamlit Community Cloud setup.