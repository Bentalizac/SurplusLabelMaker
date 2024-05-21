### For whoever has to deal with this next. This whole thing is taking the guts out of the brother_ql package to make it run as a script instead of as a commandline prompt. There's probably an easier way, but this needed to compile down.
def printLabel():
    from brother_ql.conversion import convert
    from brother_ql.backends.helpers import send
    from brother_ql.raster import BrotherQLRaster

    # Hardcoded values for the arguments
    images = ["printReadyLabel.png"]  # List of image paths
    label = '29'  # Example label size
    rotate = '90'  # Rotation option
    threshold = 70.0  # Threshold   
    dither = False  # Dithering flag
    compress = False  # Compression flag
    red = False  # Red printing flag
    dpi_600 = False  # 600 DPI flag
    lq = False  # Low quality flag
    no_cut = False  # No cut flag

    # Simulating ctx.meta values (replace these with actual values or environment variables as needed)
    backend = 'network'
    model = 'QL-710W'
    printer = 'tcp://192.168.0.43'

    def main():
        qlr = BrotherQLRaster(model)
        qlr.exception_on_warning = True

        # Prepare kwargs dictionary with hardcoded values
        kwargs = {
            'images': images,
            'label': label,
            'rotate': rotate,
            'threshold': threshold,
            'dither': dither,
            'compress': compress,
            'red': red,
            'dpi_600': dpi_600,
            'lq': lq,
            'cut': not no_cut
        }

        # Convert the images
        instructions = convert(qlr=qlr, **kwargs)
        # Send the instructions to the printer
        send(instructions=instructions, printer_identifier=printer, backend_identifier=backend, blocking=True)


    main()