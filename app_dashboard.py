import streamlit as st
import awesome_streamlit as ast
import src.pages.home_page
import src.pages.predict

ast.core.services.other.set_logging_format()

# create the choices
PAGES = {
    "Home": src.pages.home_page,
    "Run Predictions": src.pages.predict
}


# render the pages
def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This App is an end-to-end product that enables the Rossmann pharmaceutical company to 
        view predictions on sales across their stores.
"""
    )

# run it
if __name__ == "__main__":
    main()