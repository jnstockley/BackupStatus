import config.config as config


def main():
    config.load_config()
    config.set_profile()
    config.get_value("servers.server")


if __name__ == '__main__':
    main()
