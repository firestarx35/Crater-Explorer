from ultralytics import YOLO
model_mars = YOLO('best.pt')
model_moon = YOLO('moon_model.pt')
#model.predict(source = 'images',hide_labels = True,line_thickness = 2,save = True,save_txt = True)
