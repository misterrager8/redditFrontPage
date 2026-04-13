import setuptools

setuptools.setup(
    name="redditdash",
    py_modules=["reddit_dash"],
    long_description=open("README.md").read(),
    license=open("LICENSE.md").read(),
    entry_points={"console_scripts": ["redditdash=reddit_dash.__main__:cli"]},
)
