import re

from django.shortcuts import render,HttpResponse,redirect
from django.utils.deprecation import MiddlewareMixin

class ValidPermission(MiddlewareMixin):

    def process_request(self,request):

        current_path = request.path_info

        # 白名单验证
        valid_list = ['/login/','/register/','/admin/.*']
        for url in valid_list:
            if re.match(url,current_path):
                return None

        # 用户登录验证
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login/')

        # 权限验证
        flag = False
        bar_list = [
            {'title':'首页','url':'#'}
        ]
        url_dict = request.session.get('urls_dict')
        for item in url_dict.values():
            url = '^%s$'%item['url']
            if re.match(url,current_path):
                flag = True
                request.menu_id = item['pid'] or item['id']
                if not item['pid']:
                    bar_list.extend([{'title':item['title'],'url':item['url'],'class':'active'}])
                else:
                    bar_list.extend([{'title':item['p_title'],'url':item['p_url']},
                                    {'title':item['title'],'url':item['url'],'class':'active'}])
                request.bar_list = bar_list
                break
        if not flag:
            return HttpResponse('没有访问权限')
