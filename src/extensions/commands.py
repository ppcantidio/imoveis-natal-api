def init_app(app):
    # add multiple commands in a bulk
    for command in []:
        app.cli.add_command(app.cli.command()(command))
