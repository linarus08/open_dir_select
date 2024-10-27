from win32comext.shell import shell, shellcon


def open_folder_and_select_items(path, files_to_select):
    """Открыть папку и выделить файлы"""
    path_pidl = shell.SHILCreateFromPath(path, shellcon.SFGAO_FOLDER)[0]
    desktop = shell.SHGetDesktopFolder()
    selected = []
    flags = shellcon.SHGDN_INFOLDER | shellcon.SHGDN_FORPARSING

    for item in desktop.BindToObject(path_pidl, None, shell.IID_IShellFolder):
        display_name = desktop.GetDisplayNameOf(item, flags)
        if display_name in files_to_select:
            selected.append(item)

    if not selected:
        selected = [path_pidl]

    shell.SHOpenFolderAndSelectItems(path_pidl, selected)


if __name__ == '__main__':
    dir_ = r"D:\Python\sign_document"
    items = ("main.py", "qwer.docx")
    open_folder_and_select_items(dir_, items)
