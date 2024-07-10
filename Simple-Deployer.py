import os
import zipfile
import random
import string
import hashlib
import requests
from datetime import datetime

def generate_hash():
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=32))
    md5_hash = hashlib.md5(random_chars.encode()).hexdigest()
    return md5_hash[:16]

def zip_folder_contents(folder_path, zip_file_name):
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, arcname=os.path.relpath(file_path, folder_path))

def zip_files(file_list, zip_file_name):
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for file_path in file_list:
            relative_path = os.path.relpath(file_path, os.path.dirname(file_list[0]))
            zipf.write(file_path, arcname=relative_path)

def calculate_md5(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        md5_hash = hashlib.md5(data).hexdigest()
    return md5_hash

def download_file(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)

user_input_path = input("Enter the path where the files are located: ").strip()

if not os.path.exists(user_input_path):
    print("Invalid path!")
    exit()

output_directory = input("Enter the output directory path: ").strip()

if not os.path.exists(output_directory):
    print("Invalid output directory!")
    exit()

deploy_history_path = input("Enter the DeployHistory directory path: ").strip()

if not os.path.exists(deploy_history_path):
    print("Invalid DeployHistory directory!")
    exit()

download_roblox_proxy = input("Do you want to download RobloxProxy.dll? (yes/no): ").strip().lower()

random_hash = generate_hash()
version_directory_path = os.path.join(output_directory, f"version-{random_hash}")
os.makedirs(version_directory_path, exist_ok=True)

if download_roblox_proxy == "yes":
    roblox_proxy_url = "https://cdn.discordapp.com/attachments/1164137026199748649/1208035026453663814/RobloxProxy.dll?ex=65e1d14a&is=65cf5c4a&hm=7e9d11b6779cdcb1addf4bc48d6df754e37e064b9bb6cd978dfa6c8344ac281b&"
    roblox_proxy_file_path = os.path.join(output_directory, "RobloxProxy.dll")
    download_file(roblox_proxy_url, roblox_proxy_file_path)
    roblox_proxy_zip_file_name = os.path.join(version_directory_path, f"version-{random_hash}-RobloxProxy.zip")
    with zipfile.ZipFile(roblox_proxy_zip_file_name, 'w') as zipf:
        zipf.write(roblox_proxy_file_path, arcname="RobloxProxy.dll")
    os.remove(roblox_proxy_file_path)

# TODO: Make this better but i'm lazy rn. Special thanks to Shi for the RbxManifest maker.
specified_files = [
    "ReflectionMetadata.xml",
    "RobloxPlayerBeta.exe",
    "fmod.dll",
    "content\\fonts\\arial.ttf",
    "content\\fonts\\arialbd.ttf",
    "content\\fonts\\characterCameraScript.rbxmx",
    "content\\fonts\\characterControlScript.rbxmx",
    "content\\fonts\\gamecontrollerdb.txt",
    "content\\fonts\\humanoidSoundNewLocal.rbxmx",
    "content\\fonts\\SourceSansPro-Bold.ttf",
    "content\\fonts\\SourceSansPro-It.ttf",
    "content\\fonts\\SourceSansPro-Light.ttf",
    "content\\fonts\\SourceSansPro-Regular.ttf",
    "content\\sky\\moon.jpg",
    "content\\sky\\sun.jpg",
    "content\\sounds\\action_falling.mp3",
    "content\\sounds\\action_footsteps_plastic.mp3",
    "content\\sounds\\action_get_up.mp3",
    "content\\sounds\\action_jump.mp3",
    "content\\sounds\\action_jump_land.mp3",
    "content\\sounds\\action_swim.mp3",
    "content\\sounds\\impact_explosion_03.mp3",
    "content\\sounds\\impact_water.mp3",
    "content\\sounds\\snap.mp3",
    "content\\sounds\\uuhhh.mp3",
    "shaders\\shaders_d3d11.pack",
    "shaders\\shaders_d3d9.pack",
    "shaders\\shaders_glsl.pack",
    "shaders\\shaders_glsl3.pack",
    "content\\textures\\advancedMove.png",
    "content\\textures\\advancedMove_joint.png",
    "content\\textures\\advancedMove_keysOnly.png",
    "content\\textures\\advancedMove_noJoint.png",
    "content\\textures\\advancedMoveResize.png",
    "content\\textures\\advClosed-hand.png",
    "content\\textures\\advClosed-hand-no-weld.png",
    "content\\textures\\advClosed-hand-weld.png",
    "content\\textures\\advCursor-default.png",
    "content\\textures\\advCursor-openedHand.png",
    "content\\textures\\advCursor-white.png",
    "content\\textures\\AnchorCursor.png",
    "content\\textures\\ArrowCursor.png",
    "content\\textures\\ArrowCursorDecalDrag.png",
    "content\\textures\\ArrowFarCursor.png",
    "content\\textures\\blackBkg_round.png",
    "content\\textures\\blackBkg_square.png",
    "content\\textures\\Blank.png",
    "content\\textures\\chatBubble_bot_notifyGray_dotDotDot.png",
    "content\\textures\\explosion.png",
    "content\\textures\\face.png",
    "content\\textures\\FlatCursor.png",
    "content\\textures\\glow.png",
    "content\\textures\\gradient.png",
    "content\\textures\\HingeCursor.png",
    "content\\textures\\LockCursor.png",
    "content\\textures\\MotorCursor.png",
    "content\\textures\\MouseLockedCursor.png",
    "content\\textures\\rotationArrow.png",
    "content\\textures\\sparkle.png",
    "content\\textures\\SurfacesDefault.png",
    "content\\textures\\transformFiveDegrees.png",
    "content\\textures\\transformNinetyDegrees.png",
    "content\\textures\\transformOneDegree.png",
    "content\\textures\\transformTwentyTwoDegrees.png",
    "content\\textures\\UnAnchorCursor.png",
    "content\\textures\\UnlockCursor.png",
    "content\\textures\\WeldCursor.png",
    "content\\textures\\whiteCircle.png",
    "PlatformContent\\pc\\textures\\studs.dds",
    "PlatformContent\\pc\\textures\\wangIndex.dds",
    "PlatformContent\\pc\\terrain\\diffuse.dds",
    "PlatformContent\\pc\\terrain\\materials.json",
    "PlatformContent\\pc\\terrain\\normal.dds",
    "PlatformContent\\pc\\terrain\\specular.dds"
]

found_files = []
for root, _, files in os.walk(user_input_path):
    for file in files:
        if file in specified_files:
            found_files.append(os.path.join(root, file))

zip_files(found_files, os.path.join(version_directory_path, f"version-{random_hash}-RobloxApp.zip"))

shaders_folder_path = os.path.join(user_input_path, "shaders")
zip_folder_contents(shaders_folder_path, os.path.join(version_directory_path, f"version-{random_hash}-shaders.zip"))

content_folder_path = os.path.join(user_input_path, "content")
for folder_name in os.listdir(content_folder_path):
    folder_path = os.path.join(content_folder_path, folder_name)
    if os.path.isdir(folder_path):
        zip_folder_contents(folder_path, os.path.join(version_directory_path, f"version-{random_hash}-content-{folder_name}.zip"))

textures_zip_path = os.path.join(version_directory_path, f"version-{random_hash}-content-textures.zip")
textures2_zip_path = os.path.join(version_directory_path, f"version-{random_hash}-content-textures2.zip")
with zipfile.ZipFile(textures_zip_path, 'r') as zip_read:
    with zipfile.ZipFile(textures2_zip_path, 'w') as zip_write:
        for file in zip_read.infolist():
            zip_write.writestr(file, zip_read.read(file))

dll_files = [file for file in os.listdir(user_input_path) if file.endswith(".dll")]
zip_file_name = os.path.join(version_directory_path, f"version-{random_hash}-Libraries.zip")
with zipfile.ZipFile(zip_file_name, 'w') as zipf:
    for dll_file in dll_files:
        dll_file_path = os.path.join(user_input_path, dll_file)
        zipf.write(dll_file_path, arcname=os.path.basename(dll_file_path))

terrain_folder_path = os.path.join(user_input_path, "PlatformContent", "pc", "terrain")
zip_folder_contents(terrain_folder_path, os.path.join(version_directory_path, f"version-{random_hash}-content-terrain.zip"))

textures_folder_path = os.path.join(user_input_path, "PlatformContent", "pc", "textures")
zip_folder_contents(textures_folder_path, os.path.join(version_directory_path, f"version-{random_hash}-content-textures3.zip"))

rbx_manifest_file = os.path.join(version_directory_path, "rbxManifest.txt")
with open(rbx_manifest_file, "w") as output_file:
    for file_path in specified_files:
        full_path = os.path.join(user_input_path, file_path)
        try:
            md5_hash = calculate_md5(full_path)
            output_file.write(f"{file_path}\n{md5_hash}\n")
        except FileNotFoundError:
            output_file.write(f"{file_path}\nFile not found\n")

version_file_path = os.path.join(version_directory_path, "version")
with open(version_file_path, "w") as version_file:
    version_file.write(f"version-{random_hash}")

deploy_history_file_path = os.path.join(deploy_history_path, "DeployHistory.txt")
current_time = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
deploy_message = f"New Client version-{random_hash} at {current_time}... Done!\n"

if os.path.exists(deploy_history_file_path):
    with open(deploy_history_file_path, "a") as deploy_history_file:
        deploy_history_file.write(deploy_message)
else:
    with open(deploy_history_file_path, "w") as deploy_history_file:
        deploy_history_file.write(deploy_message)

print("rbxManifest.txt, version file, DeployHistory updated successfully, and RobloxProxy.zip created.")
