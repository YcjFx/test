import unittest
import minium


class Mytest(minium.MiniTest):

    def test_log_in(self): #测试登录功能
        button_log_in = self.page.get_element('button.button-xy')  # 选择登录页面按钮
        button_log_in.click()
        self.assertEqual(self.page, "pages/index/index")

    def test_homepage_loading(self):
        url = '/pages/index/index'
        self.app.relaunch(url)
        self.assertEqual(True, self.page.element_is_exists('view.list-item', max_timeout=3))

    def test_view_products(self):
        url = '/pages/index/index'
        self.app.relaunch(url)
        text = self.page.get_element('text.item-title', text_contains='库洛米', max_timeout=3)  # 选择男士羽绒服
        text.click()
        self.page.wait_for('text.commodity-desc', max_timeout=3)
        text = self.page.get_element('text.commodity-desc')
        self.assertIn('库洛米', text.inner_text)

    def test_collect(self):
        url = '/pages/index/index'
        self.app.relaunch(url)
        text = self.page.get_element('text.item-title', text_contains='小熊意式咖啡机', max_timeout=3)  # 选择商品
        text.click()
        collect = self.page.get_element('image.collect-flag', max_timeout=3)
        collect.click()
        url = "/pages/my/collect/collect"
        self.app.relaunch(url)
        self.assertEqual(True, self.page.element_is_exists('text.item-title', text_contains="小熊意式咖啡机", max_timeout=3))

    def test_worth(self):
        url = '/pages/index/index'
        self.app.relaunch(url)
        text = self.page.get_element('text.item-title', text_contains='小熊意式咖啡机', max_timeout=3)  # 选择商品
        text.click()
        text_zhi = self.page.get_element('text.isnot-radio')
        zhi1 = float(text_zhi.inner_text.strip('%'))
        button = self.page.get_element('button.btn', inner_text="不值", max_timeout=3)
        button.click()
        zhi2 = float(text_zhi.inner_text.strip('%'))
        self.assertLess(zhi1, zhi2)

if __name__ == '__main__':
    unittest.main()  # 启动测试框架
