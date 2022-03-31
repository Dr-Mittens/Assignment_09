#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (James Miller, 3/30/22, Added track compatability)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        IO.ScreenIO.print_CD_menu()
        subChoice = IO.ScreenIO.menu_CD_choice()
        if subChoice == 'x':
            break
        if subChoice == 'a':
            newtrack = IO.ScreenIO.get_track_info()
            PC.DataProcessor.add_track(newtrack, cd)
        elif subChoice == 'd':
            try:
                IO.ScreenIO.show_tracks(cd)
            except:
                print('No tracks saved for this Album')
        elif subChoice == 'r':
            IO.ScreenIO.show_tracks(cd)
            target = input('Please enter the ID of the track you want removed: ')
            cd.DC.CD.rmv_track(target)
        else:
            print('Error with executing CD command')

    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')