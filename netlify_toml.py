# Python script to generate netlify.toml

def create_netlify_toml():
    content = """
[build]
  # Define the base directory where Netlify should find your code
  publish = "/"
  command = "streamlit run app.py"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
"""
    # Write the content to a file named netlify.toml
    with open("netlify.toml", "w") as f:
        f.write(content)

    print("netlify.toml has been created!")

# Run the function
create_netlify_toml()
