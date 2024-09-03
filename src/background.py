import pyopencl as cl
import numpy as np
import pygame




def create_context(width, height):
    platform = cl.get_platforms()[0]
    device = platform.get_devices()[0]
    context = cl.Context([device])
    queue = cl.CommandQueue(context)

    kernel_source = """
    __kernel void setPixels(__global uchar4* pixels, int width, int height, float time) {
        int x = get_global_id(0);
        int y = get_global_id(1);
        int idx = y * width + x;
        float cx = width / 2.0f;
        float cy = height / 2.0f;
        float s = sin(time);
        float c = cos(time);
        float nx = c * (x - cx) - s * (y - cy) + cx;
        float ny = s * (x - cx) + c * (y - cy) + cy;
        uchar r = (uchar)(255 * (nx / (float)width));
        uchar g = (uchar)(255 * (ny / (float)height));
        pixels[idx] = (uchar4)(r, g, 190, 255);
    }
    """

    program = cl.Program(context, kernel_source).build()

    pixels = np.zeros((height, width, 4), dtype=np.uint8)
    pixels_buffer = cl.Buffer(context, cl.mem_flags.WRITE_ONLY, pixels.nbytes)

    return queue, program, pixels_buffer

def run_kernel(queue, program, pixels_buffer, width, height, time, screen):
    program.setPixels(queue, (width, height), None,
                        pixels_buffer, 
                        np.int32(width), 
                        np.int32(height), 
                        np.float32(time))
    
    result = np.empty((height, width, 4), dtype=np.uint8)
    cl.enqueue_copy(queue, result, pixels_buffer)
    surface = pygame.image.frombuffer(result.tobytes(), (width, height), 'RGBA')
    screen.blit(surface, (0, 0))

    s = pygame.Surface((width - 32, height - 32), pygame.SRCALPHA)
    s.fill((255, 255, 255, 100))
    screen.blit(s, (16, 16))
