from selene import browser, be, have


browser.open('https://duckduckgo.com')
browser.element('[name="q"]').should(be.blank).type('рррррррррвbbnnnjjыароврыаовыаолывмиорвалимлроваиморвиаромиваимлваимливаимлравимрвыаимрва').press_enter()
browser.element('html').should(have.text('все нашwffdff!'))