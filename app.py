import streamlit as st

TEMPLATE = open("codemagic-template.yaml").read()

st.title("Codemagic.yaml Generator")

apikey = st.text_input("APIKEY NAME")
bundle = st.text_input("Bundle ID")
appid = st.text_input("App ID")
project = st.text_input("Xcode Project / Scheme (без .xcodeproj)")

EMAIL = st.secrets.get("EMAIL", "{EMAIL}")

if apikey and bundle and appid and project:
    yaml = TEMPLATE \
        .replace("{APIKEY_NAME}", apikey) \
        .replace("{BUNDLE_ID}", bundle) \
        .replace("{APP_ID}", appid) \
        .replace("{PROJECT_NAME}", project) \
        .replace("{EMAIL}", EMAIL)

    st.subheader("Generated codemagic.yaml")
    st.code(yaml, language="yaml")
else:
    st.info("Fill all fields to see the result 👇")
