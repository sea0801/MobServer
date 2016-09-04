# -*- coding: utf-8 -*-
import os
from operator import itemgetter
from config.config import *
import xmltodict
from config.config import DISTRI_APP_PATH

def xml_reader(xml_path):
    f = open(xml_path, 'r')
    content = f.read()
    f.close()
    app_info_dict = xmltodict.parse(content, encoding='utf-8')
    return app_info_dict


def get_packages(app_path, name, type):
    app_list = []
    pv_list = []
    if os.path.isdir(app_path):
        package_versions = os.listdir(app_path)
        for pv in package_versions:
            if os.path.isdir(app_path + '/' + pv):
                pv_info = xml_reader(app_path + '/' + pv + '/' + get_ext_file(app_path + '/' + pv, 'xml'))
                size = pv_info['config']['app']['size']
                released = pv_info['config']['app']['released']
                if type == 'android':
                    apk_file = str(get_ext_file(app_path + '/' + pv, 'apk'))
                    pv_list.append({'version': pv,
                                    'size': size,
                                    'released': released,
                                    'package_url': 'https://' + SERVER_IP + '/' + DISTRI_APP_PATH + '/' + type +
                                                   '/' + name + '/' + pv + '/' + apk_file,
                                    'package_path': DISTRI_APP_PATH + '/' + type + '/' + name + '/' + pv + '/' + apk_file
                                    })
                if type == 'ios':
                    ipa_file = str(get_ext_file(app_path + '/' + pv, 'ipa'))
                    pro_file = (get_ext_file(app_path , 'mobileprovision'))
                    plist_file = str(get_ext_file(app_path + '/' + pv, 'plist'))
                    pv_list.append({'version': pv,
                                    'size': size,
                                    'released': released,
                                    'package_path': DISTRI_APP_PATH + '/' + type + '/' + name + '/' + pv + '/' + ipa_file,
                                    'package_url': 'itms-services://?action=download-manifest&url=https://' + SERVER_IP +
                                                   '/' + DISTRI_APP_PATH + '/' + type + '/' + name + '/' + pv + '/' + plist_file,
                                    'mobileprovision': '' if pro_file == None else (DISTRI_APP_PATH + '/' + type + '/' + name + '/' + pro_file)
                                    })
        app_info = xml_reader(app_path + '/' + get_ext_file(app_path, 'xml'))
        description = app_info['config']['app']['description']
        packages = sorted(pv_list, key=itemgetter('released'), reverse=True)
        image_file = str(get_ext_file(app_path, 'png'))
        app_list.append({'name': name, 'type': type, 'description': description,
                         'package': packages,
                         'last_build': packages[0]['released'],
                         'image': DISTRI_APP_PATH + '/' + type + '/' + name + '/' + image_file
                         })
    return app_list


def get_apps(distri_path):
    dir_list = {}
    app_list = []
    if os.path.isdir(distri_path + '/android'):
        dir_list['android'] = os.listdir(distri_path + '/android')
    if os.path.isdir(distri_path + '/ios'):
        dir_list['ios'] = os.listdir(distri_path + '/ios')
    if dir_list.has_key('android') and dir_list['android'] != []:
        for d in dir_list['android']:
            pv_list = []
            if os.path.isdir(distri_path + '/android/' + d):
                package_versions = os.listdir(distri_path + '/android/' + d)
                for pv in package_versions:
                    if os.path.isdir(distri_path + '/android/' + d + '/' + pv):
                        pv_info = xml_reader(distri_path + '/android/' + d + '/' + pv + '/' +
                                             get_ext_file(distri_path + '/android/' + d + '/' + pv, 'xml'))
                        size = pv_info['config']['app']['size']
                        released = pv_info['config']['app']['released']
                        apk_file = str(get_ext_file(distri_path + '/android/' + d + '/' + pv, 'apk'))
                        pv_list.append({'version': pv,
                                        'size': size,
                                        'released': released,
                                        'package_url': 'https://' + SERVER_IP + '/' + DISTRI_APP_PATH +
                                                       '/android/' + d + '/' + pv + '/' + apk_file,
                                        'package_path': DISTRI_APP_PATH + '/android/' + d + '/' + pv + '/' + apk_file
                                        })
                app_info = xml_reader(
                    distri_path + '/android/' + d + '/' + get_ext_file(distri_path + '/android/' + d, 'xml'))
                description = app_info['config']['app']['description']
                last_build = app_info['config']['app']['lastbuild']
                packages = sorted(pv_list, key=itemgetter('released'), reverse=True)
                image_file = str(get_ext_file(distri_path + '/android/' + d, 'png'))
                app_list.append({'name': d, 'type': 'android', 'description': description,
                                 'package': packages,
                                 'last_build': packages[0]['released'],
                                 'image': DISTRI_APP_PATH + '/android/' + d + '/' + image_file
                                 })

    if dir_list.has_key('ios') and dir_list['ios'] != []:
        for d in dir_list['ios']:
            pv_list = []
            if os.path.isdir(distri_path + '/ios/' + d):
                package_versions = os.listdir(distri_path + '/ios/' + d)
                for pv in package_versions:
                    if os.path.isdir(distri_path + '/ios/' + d + '/' + pv):
                        pv_info = xml_reader(distri_path + '/ios/' + d + '/' + pv + '/' +
                                             get_ext_file(distri_path + '/ios/' + d + '/' + pv, 'xml'))
                        size = pv_info['config']['app']['size']
                        released = pv_info['config']['app']['released']
                        ipa_file = str(get_ext_file(distri_path + '/ios/' + d + '/' + pv, 'ipa'))
                        pro_file = (get_ext_file(distri_path + '/ios/' + d, 'mobileprovision'))
                        plist_file = str(get_ext_file(distri_path + '/ios/' + d + '/' + pv, 'plist'))
                        pv_list.append({'version': pv,
                                        'size': size,
                                        'released': released,
                                        'package_path': DISTRI_APP_PATH + '/ios/' + d + '/' + pv + '/' + ipa_file,
                                        'package_url': 'itms-services://?action=download-manifest&url=https://' +
                                                       SERVER_IP + '/' + DISTRI_APP_PATH + '/ios/' + d + '/' + pv + '/' + plist_file,
                                        'mobileprovision': '' if pro_file == None else (DISTRI_APP_PATH + '/ios/' + d + '/' + pro_file)
                                        })
                app_info = xml_reader(distri_path + '/ios/' + d + '/' + get_ext_file(distri_path + '/ios/' + d, 'xml'))
                description = app_info['config']['app']['description']
                packages = sorted(pv_list, key=itemgetter('released'), reverse=True)
                image_file = str(get_ext_file(distri_path + '/ios/' + d, 'png'))
                app_list.append({'name': d, 'type': 'ios', 'description': description,
                                 'package': packages,
                                 'last_build': packages[0]["released"],
                                 'image': DISTRI_APP_PATH + '/ios/' + d + '/' + image_file
                                 })
    return sorted(app_list, key=itemgetter('last_build'), reverse=True)


def get_ext_file(file_path, file_type):
    file_type = '.' + file_type
    if os.path.isdir(file_path):
        files = os.listdir(file_path)
        for file in files:
            if not os.path.isdir(file_path + '/' + file):
                f_name, f_type = os.path.splitext(file)
                if f_type == file_type:
                    return file
    return None


if __name__ == '__main__':
    pass