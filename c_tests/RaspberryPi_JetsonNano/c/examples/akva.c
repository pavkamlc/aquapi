/*****************************************************************************
* | File      	:   EPD_2IN7_test.c
* | Author      :   Waveshare team
* | Function    :   1.54inch e-paper test demo
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2019-06-11
* | Info        :
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
******************************************************************************/
#include "EPD_2in7.h"

#include "DEV_Config.h"
#include "GUI_Paint.h"
#include "GUI_BMPfile.h"
#include "ImageData.h"
#include <time.h>
#include <stdlib.h> // malloc() free()
#include <stdio.h>


int akva(void)
{
    printf("Akva service\r\n");
    if(DEV_Module_Init()!=0){
        return -1;
    }

    printf("e-Paper Init and Clear...\r\n");
    EPD_2IN7_Init();
    EPD_2IN7_Clear();
    DEV_Delay_ms(500);

    //Create a new image cache
    UBYTE *BlackImage;
    /* you have to edit the startup_stm32fxxx.s file and set a big enough heap size */
    
    printf("show Gray-%d-\r\n", index);
    UWORD Imagesize = ((EPD_2IN7_WIDTH % 4 == 0)? (EPD_2IN7_WIDTH / 4 ): (EPD_2IN7_WIDTH / 4 + 1)) * EPD_2IN7_HEIGHT;
    if((BlackImage = (UBYTE *)malloc(Imagesize)) == NULL) {
        printf("Failed to apply for black memory...\r\n");
        return -1;
    }
    printf("4 grayscale display\r\n");
    EPD_2IN7_Init_4Gray();
    //EPD_2IN7_Init();

    //Paint_NewImage(BlackImage, EPD_2IN7_WIDTH, EPD_2IN7_HEIGHT, ROTATE_270, WHITE);
    //Paint_SetScale(3);
    //Paint_Clear(WHITE);
    //GUI_ReadBmp_4Gray("./pic/2in7_aqua4.bmp", 0, 0);

    Paint_NewImage(BlackImage, EPD_2IN7_WIDTH, EPD_2IN7_HEIGHT, ROTATE_270, GRAY4);
    Paint_SetScale(4);
    Paint_Clear(GRAY4);

    int index = 0;
    while(index < 50)
	{
        printf("index %d\n\r", index);

	Paint_DrawPoint(10, 100, GRAY4, DOT_PIXEL_3X3, DOT_STYLE_DFT);
	Paint_DrawLine(70, 70, 20, 120, GRAY4, DOT_PIXEL_1X1, LINE_STYLE_SOLID);
	Paint_DrawRectangle(80, 70, 130, 120, GRAY4, DOT_PIXEL_1X1, DRAW_FILL_FULL);
	Paint_DrawCircle(105, 95, 20, GRAY2, DOT_PIXEL_1X1, DRAW_FILL_FULL);

	char time[11];
	struct timespec now;
	clock_gettime(CLOCK_REALTIME, &now);
	struct tm *tmnow = localtime(&now);
	sprintf(time, "Cas: %d:%d", tmnow->tm_hour, tmnow->tm_min);
        Paint_DrawString_EN(10, 10, time, &Font24, GRAY1, GRAY4);

	char temp[11];
	sprintf(temp, "Teplota: %d", index);
        Paint_DrawString_EN(10, 30, temp, &Font20, GRAY1, GRAY4);

	Paint_DrawString_EN(10, 50, "Vlhkost: ", &Font12, GRAY4, GRAY1);

        Paint_DrawString_EN(10, 70, "Hladina: ", &Font16, GRAY4, GRAY1);

        Paint_DrawNum(10, 90, 987654321, &Font16, GRAY4, GRAY1);

	EPD_2IN7_4GrayDisplay(BlackImage);
	//EPD_2IN7_Display(BlackImage);

        DEV_Delay_ms(3000);

	index = index + 1;
    }

    EPD_2IN7_Clear();

    // close 5V
    printf("Goto Sleep...\r\n");
    EPD_2IN7_Sleep();
    free(BlackImage);
    BlackImage = NULL;
    DEV_Delay_ms(2000);//important, at least 2s
    printf("close 5V, Module enters 0 power consumption ...\r\n");
    DEV_Module_Exit();

    return 0;
}

