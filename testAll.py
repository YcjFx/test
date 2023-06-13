import unittest
import minium


class Mytest(minium.MiniTest):

    def test_log_in(self): #用户登录
        button_log_in = self.page.get_element('button.button-xy')  # 选择登录页面按钮
        button_log_in.click()
        self.assertEqual(self.page, "pages/index/index")

    def test_homepage_loading(self):#主页商品加载
        url = '/pages/index/index'
        self.app.relaunch(url)
        self.assertEqual(True, self.page.element_is_exists('view.list-item', max_timeout=3))

    def test_view_products(self):#进入商品详情页面
        url = '/pages/index/index'
        self.app.relaunch(url)
        text = self.page.get_element('text.item-title', text_contains='小熊意式咖啡机', max_timeout=3)  #
        text.click()
        self.page.wait_for('text.commodity-price', max_timeout=3)
        text = self.page.get_element('text.commodity-price', text_contains='小熊意式咖啡机')
        self.assertIn('小熊意式咖啡机', text.inner_text)

    def test_search(self): #搜索功能
        url = '/pages/index/index'
        self.app.relaunch(url)
        input = self.page.get_element('input.search-input', max_timeout=3)  # 选择搜索框
        input.input("YSL圣罗兰")
        button = self.page.get_element('button.search-btn', max_timeout=3) #搜索按钮
        button.click()
        self.assertEqual(True, self.page.element_is_exists('text.item-title', text_contains="YSL圣罗兰",
                                                           max_timeout=3))

    def test_worth(self):
        url = '/pages/index/index'
        self.app.relaunch(url)
        text = self.page.get_element('text.item-title', text_contains='小熊意式咖啡机', max_timeout=3)  # 选择商品
        text.click()
        text_zhi = self.page.get_element('text.is-radio') #值的按钮
        zhi1 = float(text_zhi.inner_text.strip('%'))
        button = self.page.get_element('button.btn', inner_text="值", max_timeout=3)
        button.click()
        zhi2 = float(text_zhi.inner_text.strip('%'))
        self.assertLess(zhi1, zhi2)

    def test_isnotworth(self):
        url = '/pages/index/index'
        self.app.relaunch(url)
        text = self.page.get_element('text.item-title', text_contains='小熊意式咖啡机', max_timeout=3)  # 选择商品
        text.click()
        text_zhi = self.page.get_element('text.isnot-radio') #不值的按钮
        zhi1 = float(text_zhi.inner_text.strip('%'))
        button = self.page.get_element('button.btn', inner_text="不值", max_timeout=3)
        button.click()
        zhi2 = float(text_zhi.inner_text.strip('%'))
        self.assertLess(zhi1, zhi2)

    def test_collect(self):#收藏商品
        url = '/pages/index/index'
        self.app.relaunch(url)
        text = self.page.get_element('text.item-title', text_contains='小熊意式咖啡机', max_timeout=3)  # 选择商品
        text.click()
        collect = self.page.get_element('image.collect-flag', max_timeout=3)
        collect.click()
        url = "/pages/my/collect/collect"
        self.app.relaunch(url)
        self.assertEqual(True, self.page.element_is_exists('text.item-title', text_contains="小熊意式咖啡机", max_timeout=3))

    def test_Price_curve(self): #查看价格曲线
        url = '/pages/index/index'
        self.app.relaunch(url)
        text = self.page.get_element('text.item-title', text_contains='小熊意式咖啡机', max_timeout=3)  # 选择商品
        text.click()
        self.assertEqual(True, self.page.element_is_exists('canvas.', max_timeout=3))

    def test_comment(self): #他人评论
        url = '/pages/index/index'
        self.app.relaunch(url)
        text = self.page.get_element('text.item-title', text_contains='小熊意式咖啡机', max_timeout=3)  # 选择商品
        text.click()
        self.assertEqual(True, self.page.element_is_exists('text.comment-text', max_timeout=3))

    def test_comment2(self):#发布评论
        url = '/pages/index/index'
        self.app.relaunch(url)
        text = self.page.get_element('text.item-title', text_contains='Apple', max_timeout=3)  # 选择商品
        text.click()
        input = self.page.get_element('input.comment-input')
        input.input("我认为这部手机很值")
        button = self.page.get_element('button.input-button')
        button.click()
        self.assertEqual(True, self.page.element_is_exists('text.comment-text', text_contains="我认为这部手机很值", max_timeout=3))

    def test_cancel(self):
        url = '/pages/publish/publish'
        self.app.relaunch(url)
        button_cancel = self.page.get_element('button.cancel', max_timeout=3)  # 选择取消按钮
        button_cancel.click()
        self.assertEqual(self.page, "pages/index/index")


if __name__ == '__main__':
    unittest.main()  # 启动测试框架
