from django import template

register = template.Library()


# 실제 템플릿에서 사용할 수 있도록 template.Library의 filter 데코레이터 적용
@register.filter
def query_string(q):
<<<<<<< HEAD
    # value에는 QueryDict가 온다
=======
    # q에는 QueryDict가 온다
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
    # str.join()과 리스트 컴프리헨션으로 한줄로 줄여보세요
    # ret = '?'
    # for k, v_list in q.lists():
    #     for v in v_list:
    #         ret += '&{}={}'.format(k, v)
    # return ret
<<<<<<< HEAD
    return '?' + '&'.join(['{}={}'.format(k, v) for k, v_list in q.lists() for v in v_list])
=======
    return '?' + '&'.join(['{}={}'.format(k, v) for k, v_list in q.lists() for v in v_list])
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
