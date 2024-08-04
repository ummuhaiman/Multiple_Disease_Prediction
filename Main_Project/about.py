import streamlit as st

def main():
    # Display text paragraph
    st.write("Welcome to Health Cure, where our mission is to empower individuals with proactive health insights. "
             "Our journey began with a shared vision of harnessing cutting-edge algorithms and machine learning "
             "methodologies to create a comprehensive disease prediction platform. We continuously refine and "
             "expand our predictive capabilities. Our commitment extends beyond technology, embracing a user-centric "
             "approach that values transparency and user feedback. As we look to the future, our vision is to evolve "
             "this platform, contribute to healthcare advancements, and make a positive impact on global well-being. "
             "Thank you for joining us on this transformative health journey.")

    # Add some vertical spacing after the paragraph
    st.write("")

    # Display an image
    st.image("aboutimg.jpg",use_column_width=True)

if __name__ == "__main__":
    main()

