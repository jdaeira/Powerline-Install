from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    """Basic theme which only uses colors in 0-15 range"""
    USERNAME_FG = 0
    USERNAME_BG = 112   
    USERNAME_ROOT_BG = 0

    HOSTNAME_FG = 0
    HOSTNAME_BG = 112

    HOME_SPECIAL_DISPLAY = False
    PATH_BG = 75  # dark grey
    PATH_FG = 15  # light grey
    CWD_FG = 15  # white
    SEPARATOR_FG = 15

    READONLY_BG = 1
    READONLY_FG = 15

    REPO_CLEAN_BG = 2   # green
    REPO_CLEAN_FG = 0   # black
    REPO_DIRTY_BG = 1   # red
    REPO_DIRTY_FG = 15  # white

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = 0
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 11
    CMD_FAILED_FG = 0

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0

    AWS_PROFILE_FG = 14
    AWS_PROFILE_BG = 8

    TIME_FG = 8
    TIME_BG = 7
