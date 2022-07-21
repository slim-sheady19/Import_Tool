import unreal

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