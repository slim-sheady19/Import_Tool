import unreal

def print_msg(message):

    print ('the message is ' + message)

def get_assets_by_class(class_type):

    EAL = unreal.EditorAssetLibrary
    paths = EAL.list_assets('/Game/import_folder')

    assets = []

    for path in paths:
        asset_data = EAL.find_asset_data(path)
        asset_class = asset_data.asset_class
        if asset_class == class_type:
            assets.append(asset_data.get_asset())

    #for asset in assets: print (asset)
    return assets

def set_SM_properties():

    sub = unreal.StaticMeshEditorSubsystem()
    build_settings = unreal.MeshBuildSettings(use_full_precision_u_vs=True, generate_lightmap_u_vs=False)
    profile_name = unreal.CollisionProfileName

    static_meshes = get_assets_by_class('StaticMesh')
    for mesh in static_meshes:

        sub.set_lod_build_settings(mesh, 0, build_settings)