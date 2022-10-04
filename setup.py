import setuptools

setuptools.setup(
    name="RedditFrontPage",
    long_description=open("README.md").read(),
    license=open("LICENSE.md").read(),
    entry_points={"console_scripts": ["reddit=reddit_front_page.cli:run"]},
)
