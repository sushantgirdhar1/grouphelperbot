class Bot:
    token = '123456789:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    groupId = -1001234567890
    useStaffGroup = True
    staffGroupId = -1001234567890
    scanSendedFiles = True


class Databases:
    admins = 'admins.json'
    users = 'users.json'


class Messages:
    welcome = "Hi, <b>{{name}}</b>!\nWelcome in the {{group_name}} group!"


class Moderation:
    maxWarns = 3


class virusTotal:
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    apikey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'