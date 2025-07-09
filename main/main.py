from selene import browser, be, have


browser.open('https://duckduckgo.com')
browser.element('[name="q"]').should(be.blank).type('рррррррррвыароврыаовыаолывмиорвалимлроваиморвиаромиваимлваимливаимлравимрвыаимрва').press_enter()
browser.element('htmlhhsdhsdsdsd_kkksd').should(have.text('все нашлось!!!!!'))