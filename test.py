import unittest
from unittest import mock
from unittest.mock import MagicMock, Mock, patch
from main import main, create_message
import database
from GoogleAPI import APIDriveConnect

class MainTest(unittest.TestCase):

    @patch('GoogleAPI.build')
    @patch('GoogleAPI.APIDriveConnect')
    @patch('database.MySql.__new__')
    def test_main(self, mock_db, mock_api, mock_build):
        database = MagicMock()
        database.crearDB = mock.PropertyMock(return_value=None)
        database.crearDrive = mock.PropertyMock(return_value=None)
        database.crearBitacora = mock.PropertyMock(return_value=None)
        database.sqldat = mock.PropertyMock(return_value=None)
        database.sqlhist = mock.PropertyMock(return_value=None)
        database.sqlupdt = mock.PropertyMock(return_value=None)
        database.close_bd = mock.PropertyMock(return_value=None)
        
        mock_db.return_value = database

        service = MagicMock()
        service.permissions.delete.execute = mock.PropertyMock(return_value=None)
        service.files.list.execute = mock.PropertyMock(return_value=mock_items)
        service.users.messages.send.execute = mock.PropertyMock(return_value=None)
        service.build = mock.PropertyMock(return_value=None)
        
        mock_build.return_value = service

        create_message.return_value = "Este es un mensaje de prueba"
        resp = main()
        self.assertIsNone(resp)

mock_items = {'kind': 'drive#file', 'id': '1kp6HZfvTrOwauYKD593OUcYBGSghVnvPmeJnI_x-vP0', 'name': 'Prueba 2', 'mimeType': 'application/vnd.google-apps.spreadsheet', 'starred': 'False', 'trashed': 'False', 'explicitlyTrashed':
'False', 'parents': ['0ALw0qlCkITvWUk9PVA'], 'spaces': ['drive'], 'version': '5', 'webViewLink': 'https://docs.google.com/spreadsheets/d/1kp6HZfvTrOwauYKD593OUcYBGSghVnvPmeJnI_x-vP0/edit?usp=drivesdk', 'iconLink': 'https://drive-thirdparty.googleusercontent.com/16/type/application/vnd.google-apps.spreadsheet', 'hasThumbnail': 'False', 'thumbnailVersion': '0', 'viewedByMe': 'True', 'viewedByMeTime': '2020-10-31T12:29:34.942Z', 'createdTime': '2020-10-31T12:29:26.448Z', 'modifiedTime': '2020-10-31T12:29:53.222Z', 'modifiedByMeTime': '2020-10-31T12:29:53.222Z', 'modifiedByMe': 'True', 'owners': [{'kind': 'drive#user', 'displayName': 'Challenge MeLi', 'me': 'True', 'permissionId': '00478442827344784861', 'emailAddress': 'challenge.meli.2020@gmail.com'}], 'lastModifyingUser': {'kind': 'drive#user', 'displayName': 'Challenge MeLi', 'me': 'True', 'permissionId': '00478442827344784861', 'emailAddress': 'challenge.meli.2020@gmail.com'}, 'shared': 'True', 'ownedByMe': 'True', 'capabilities': {'canAddChildren': 'False', 'canAddMyDriveParent': 'False', 'canChangeCopyRequiresWriterPermission': 'True', 'canChangeViewersCanCopyContent': 'True', 'canComment': 'True', 'canCopy': 'True', 'canDelete': 'True', 'canDownload': 'True', 'canEdit': 'True', 'canListChildren': 'False', 'canModifyContent': 'True', 'canMoveChildrenWithinDrive': 'False', 'canMoveItemIntoTeamDrive': 'True', 'canMoveItemOutOfDrive': 'True', 'canMoveItemWithinDrive': 'True', 'canReadRevisions': 'True', 'canRemoveChildren': 'False', 'canRemoveMyDriveParent': 'True', 'canRename': 'True', 'canShare': 'True', 'canTrash': 'True', 'canUntrash': 'True'}, 'viewersCanCopyContent': 'True', 'copyRequiresWriterPermission': 'False', 'writersCanShare': 'True', 'permissions': [{'kind': 'drive#permission', 'id': 'anyoneWithLink', 'type': 'anyone', 'role': 'reader', 'allowFileDiscovery': 'False'}, {'kind': 'drive#permission', 'id': '00478442827344784861', 'type': 'user', 'emailAddress': 'challenge.meli.2020@gmail.com', 'role': 'owner', 'displayName': 'Challenge MeLi', 'deleted': 'False'}], 'permissionIds': ['anyoneWithLink', '00478442827344784861'], 'quotaBytesUsed': '0', 'isAppAuthorized': 'False'}

