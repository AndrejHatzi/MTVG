import cv2

capture = cv2.CaptureFromFile("teste.mp4")
while True:
    # Need a frame to get the output video dimensions
    frame = cv2.RetrieveFrame(capture) # Will return None if there are no frames
    # New video file
    video_out = cv2.CreateVideoWriter(output_filenameX, CV_FOURCC('M','J','P','G'), capture.fps, frame.size(), 1)
    # Write the frames
    cv.WriteFrame(video_out, frame)
    while Condition2:
        frame = cv.RetrieveFrame(capture) # Will return None if there are no frames
        cv.WriteFrame(video_out, frame)