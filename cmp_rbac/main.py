import logging
import os
from cmp_rbac import config
from cmp_rbac.apis import blueprint as api_blueprint
from cmp_rbac import app

def main():
    """
    Launches flask instance (instantiating the application)
    """

    app_mode = 'development'
    if 'APP_MODE' in os.environ:
        app_mode = os.getenv('APP_MODE')

    if app_mode in config.app_config:
        app.config.from_object(config.app_config[app_mode])
    else:
        print('Application mode "{}" does not have a configuration.'.format(app_mode))


    app.register_blueprint(api_blueprint, url_prefix='/api')

    app.run(debug=True, host='127.0.0.1', port=8080)

if __name__ == '__main__':  # pragma: no cover
    main()
