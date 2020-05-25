

def test_params(params, browser):
    res = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert res, "страница товара на сайте не содержит кнопку добавления в корзину"



