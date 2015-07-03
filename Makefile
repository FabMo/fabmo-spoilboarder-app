partmaker.fma: clean *.html js/*.js css/*.css img/*.png icon.png package.json
	zip fabmo-spoilboarder-app.fma *.html js/*.js css/*.css img/*.png icon.png package.json

.PHONY: clean

clean:
	rm -rf fabmo-spoilboarder-app.fma
