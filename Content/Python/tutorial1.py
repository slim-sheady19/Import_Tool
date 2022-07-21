import unreal

def listAssetPaths(): #function declaration. print paths of all assets under project root directory

    EAL = unreal.EditorAssetLibrary #instantiate editor asset library (class?) and store in variable

    assetPaths = EAL.list_assets('/Game')

    for path in assetPaths: print (path)

def get_selection_content_browser(): #get user highlighted objects in content browser

    EUL = unreal.EditorUtilityLibrary

    selected_assets = EUL.get_selected_assets()

    for selected in selected_assets: print (selected)

def get_all_actors():

    EAS = unreal.EditorActorSubsystem()

    actors = EAS.get_all_level_actors()

    for actor in actors: print (actor)
    
def get_asset_class(class_type):

    EAL = unreal.EditorAssetLibrary
    assetPaths = EAL.list_assets('/Game')

    assets = []

    for path in assetPaths:
        asset_data = EAL.find_asset_data(path)
        asset_class = asset_data.asset_class
        if asset_class == class_type:
            assets.append(asset_data.get_asset())

    #for asset in assets: print (asset)
    return assets

def get_SM_data():

    static_meshes = get_asset_class('StaticMesh')
    for mesh in static_meshes:
        
        #import_data = mesh.get_editor_property('asset_import_data')
        #fbx_path = import_data.extract_filenames()
        #print (fbx_path)

        lod_group_info = mesh.get_editor_property('lod_group')
        print (lod_group_info)

        if lod_group_info == 'None':
            if mesh.get_num_lods() == 1:
                mesh.set_editor_property('lod_group', 'LargeProp')

def set_SM_properties():

    sub = unreal.StaticMeshEditorSubsystem()
    build_settings = unreal.MeshBuildSettings(use_full_precision_u_vs=True, generate_lightmap_u_vs=False)

    static_meshes = get_asset_class('StaticMesh')
    for mesh in static_meshes:

        sub.set_lod_build_settings(mesh, 0, build_settings)

def get_SM_instance_counts():

    level_actors = unreal.EditorActorSubsystem().get_all_level_actors()

    SM_actors = []
    SM_actor_counts = []

    for level_actor in level_actors:
        #print (level_actor.get_class().get_name())
        if (level_actor.get_class().get_name()) == 'StaticMeshActor':
            SM_component = level_actor.static_mesh_component
            SM = SM_component.static_mesh
            #print(SM.get_name())
            SM_actors.append(SM.get_name())

    processed_actors = []

    for SM_actor in SM_actors:
        if SM_actor not in processed_actors: #if statement to stop duplicate prints of same actor
            #this below print statement first prints the name (SM_actor) followed by number of instances (the .count method)
            #print(SM_actor, SM_actors.count(SM_actor))
            actor_counts = (SM_actor, SM_actors.count(SM_actor))
            SM_actor_counts.append(actor_counts)
            processed_actors.append(SM_actor)

    #sort the list before printing, starting with highest value
    SM_actor_counts.sort(key = lambda a: a[1], reverse=True)

    for item in SM_actor_counts: print (item)

def return_mat_info_SMC():

    level_actors = unreal.EditorActorSubsystem().get_all_level_actors()

    test_mat = unreal.EditorAssetLibrary.find_asset_data('/Game/M_test_Inst').get_asset()

    for level_actor in level_actors:
        if (level_actor.get_class().get_name()) == 'StaticMeshActor':
            SM_component = level_actor.static_mesh_component

            for i in range(SM_component.get_num_materials()):
                SM_component.set_material(i, test_mat)

            """
            print (level_actor.get_name())
            materials = SM_component.get_materials()
            for material in materials:
                print (material.get_name())
                try:
                    for item in material.texture_parameter_values: print (item)
                except:
                    pass
                #the try and except is to prevent any errors from stopping the script!
                print ('______')
            """