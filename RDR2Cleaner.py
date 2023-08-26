import os
import shutil

game_exe = "rdr2.exe"
current_folder = os.path.dirname(os.path.abspath(__file__))  # Get the current script's folder
destination_folder = os.path.join(current_folder, "storedMods")

vanilla_dll_list = [
    "amd_ags_x64.dll",
    "bink2w64.dll",
    "dxilconv7.dll",
    "EOSSDK-Win64-Shipping.dll",
    "ffx_fsr2_api_dx12_x64.dll",
    "ffx_fsr2_api_vk_x64.dll",
    "ffx_fsr2_api_x64.dll",
    "NvLowLatencyVk.dll",
    "nvngx_dlss.dll",
    "oo2core_5_win64.dll",
    "steam_api64.dll"
]
black_listed_suffix = [
    ".asi",
    ".ini",
    ".log",
    ".json",
    ".txt",
    ".dat"
]

file_path = os.path.join(current_folder, game_exe)


def movefile(name, reverse):
    print("Moving file: " + name)
    source_path = os.path.join(current_folder, filename)
    destination_path = os.path.join(destination_folder, filename)
    if reverse:
        shutil.move(destination_path, source_path)
        pass
    else:
        shutil.move(source_path, destination_path)
        pass


start = input("Welcome to RDR2 Cleaner\nDo you really want to move your mods? (y/n): ")
if start == "y":
    # check if the script is located in the game folder
    if os.path.isfile(file_path):
        # create storedMods folder if it doesn't exist
        if not os.path.exists(destination_folder) or not os.path.isdir(destination_folder):
            print("storeMods folder does not exist!")
            os.makedirs(destination_folder)
            print("storeMods folder has been created.")

        # check if there are files in storedMods
        files_in_stored_mods = os.listdir(destination_folder)
        files_in_stored_mods_amount = len(files_in_stored_mods)
        if files_in_stored_mods_amount == 0:
            # move files to storedMods
            for filename in os.listdir(current_folder):
                vanilla_file = False
                if filename.endswith(".dll"):
                    # check if it is a vanilla file
                    for vanilla_dll in vanilla_dll_list:
                        if vanilla_dll == filename:
                            vanilla_file = True
                            break

                    if not vanilla_file:
                        movefile(filename, False)

                else:
                    for suffix in black_listed_suffix:
                        if filename.endswith(suffix):
                            movefile(filename, False)
            print("\n\033[32mSuccessfully\033[0m moved mods to storeMods folder.")
        else:
            # move files back to game folder
            print("Moving files to game folder...")
            for filename in os.listdir(destination_folder):
                movefile(filename, True)
            print("\n\033[32mSuccessfully\033[0m moved mods back to game folder.")

input("Press enter to close this program: ")
